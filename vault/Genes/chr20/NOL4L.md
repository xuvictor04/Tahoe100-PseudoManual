---
symbol: "NOL4L"
type: "gene"
col: 12363
ensembl_id: "ENSG00000197183"
name: "nucleolar protein 4 like"
location: "20q11.21"
module: 100
arm: "+"
pooled_cpm: 35.21
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# NOL4L

*nucleolar protein 4 like* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.70× (z +11.2, q 2e-26, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.544× (z -12.7, q 3e-34, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEAD3]] (+0.68, fdr 7e-06), [[ZBTB46]] (+0.62, fdr 1e-05), [[UBTD1]] (+0.62, fdr 7e-06); moves opposite to [[TAF2]] (-0.56, fdr 1e-05), [[LDAH]] (-0.55, fdr 2e-05), [[PBRM1]] (-0.54, fdr 2e-05).
> It is in [[Module 100]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +11.2 | 2e-26 | 37/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +10.9 | 5e-25 | 38/48 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +9.0 | 3e-17 | 26/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +8.2 | 4e-14 | 34/48 (HOP62, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.8 | 1e-09 | 31/48 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.6 | 3e-04 | 21/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 6e-04 | 14/48 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.021 | 13/48 (NCI-H23, RPMI-7951, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.6 | 0.021 | 8/40 (NCI-H460, C-33 A, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.038 | 9/47 (HT-29, COLO 205, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.038 | 6/48 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.544×** | -12.7 | 3e-34 | 30/48 (HT-29, A498, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.679×** | -10.9 | 4e-25 | 34/48 (A-172, HT-29, …) | two highest doses | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.404×** | -9.8 | 1e-20 | 39/48 (Panc 03.27, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.657×** | -8.4 | 5e-15 | 22/35 (A498, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.689×** | -7.8 | 9e-13 | 27/48 (SW 1088, A498, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.673×** | -7.6 | 3e-12 | 22/41 (A498, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.689×** | -7.5 | 7e-12 | 29/48 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.721×** | -6.8 | 7e-10 | 24/45 (A498, J82, …) | all doses, flat | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.549×** | -6.5 | 5e-09 | 24/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.595×** | -5.6 | 1e-06 | 23/48 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.763×** | -5.6 | 1e-06 | 20/48 (SNU-1, LoVo, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.780×** | -5.2 | 1e-05 | 22/48 (LOX-IMVI, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.783×** | -5.1 | 2e-05 | 22/48 (HepG2/C3A, HT-29, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.794×** | -4.8 | 7e-05 | 20/48 (HepG2/C3A, SK-MEL-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.662×** | -4.5 | 3e-04 | 15/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.809×** | -4.2 | 8e-04 | 16/48 (BT-474, SK-MEL-2, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.682×** | -4.1 | 0.001 | 15/48 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.725×** | -3.5 | 0.014 | 11/48 (HepG2/C3A, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.728×** | -3.4 | 0.017 | 8/45 (H4, SK-MEL-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | 0.848× | -3.4 | 0.017 | 12/48 (SW 1271, A-427, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.889× | -3.2 | 0.033 | 10/48 (HS-578T, HOP62, …) | rises with dose | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.864× | -3.0 | 0.058 | 9/48 (A-172, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 73.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.434× (z -11.1) |
| [[J82 (line)]] | alt | 56.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[RKO (line)]] | wt | 36.9 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -11.1) |
| [[A-172 (line)]] | wt | 51.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -21.2) |
| [[CHP-212 (line)]] | wt | 83.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0747× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 158 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 69.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.4) |
| [[KATO III (line)]] | alt | 75.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 19.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +17.9) | — |
| [[Panc 03.27 (line)]] | alt | 44.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.0) |
| [[SW480 (line)]] | alt | 39.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.42× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | [[Dinaciclib (drug)]] 5 µM 0.172× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 52.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -13.2) |
| [[C32 (line)]] | wt | 19.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.5) | — |
| [[H4 (line)]] | wt | 20.3 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0951× (z -10.5) |
| [[HS-578T (line)]] | alt | 34.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -8.5) |
| [[LoVo (line)]] | wt | 21.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +15.2) | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.98× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.4) |
| [[A-427 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEAD3]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[ZBTB46]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[UBTD1]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[RGS10]] | +0.61 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TFEB]] | +0.59 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[CASZ1]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[AGAP3]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[CBL]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ARL8A]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TSPAN14]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CASTOR2]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[BAHD1]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF2]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[LDAH]] | -0.55 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[PBRM1]] | -0.54 | -0.57 / -0.49 | both halves | 2e-05 |  |
| [[BCLAF1]] | -0.54 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[MTREX]] | -0.52 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[THADA]] | -0.52 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[IFT81]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[MRPS7]] | -0.50 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ZNF252P-1]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[MRRF]] | -0.50 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[WARS2]] | -0.50 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[VPS35L]] | -0.50 | -0.48 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.4, -2.9); signed map (-19.4, 21.0). **Vector** length 112, 27.4% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.4 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.7 | +11.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +8.6 | +8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.8 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.2 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.9 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +1.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -12.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.3 | -6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -7.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.9 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar protein 4 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:32,443,059-32,585,333 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1184F4.2, DKFZP566G1424, dJ1184F4.4; previously C20orf113, C20orf112 |
| Matched by | ensembl_id |

UniProt [Q96MY1](https://www.uniprot.org/uniprotkb/Q96MY1) carries no function annotation.

**Summary**, from NCBI Gene [140688](https://www.ncbi.nlm.nih.gov/gene/140688):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16106](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16106) · Entrez [140688](https://www.ncbi.nlm.nih.gov/gene/140688) · UniProt [Q96MY1](https://www.uniprot.org/uniprotkb/Q96MY1) · Ensembl [ENSG00000197183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197183)

## Data

Gene col 12363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12363); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12363]; `tensor/DDL_lfc|DDL_z.npy` [12363]; `embed/gene_vectors.npy` [12363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12363 or target_col == 12363). Every well: [[NOL4L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOL4L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
