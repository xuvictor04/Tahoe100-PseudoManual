---
symbol: "PURB"
type: "gene"
col: 7112
ensembl_id: "ENSG00000146676"
name: "purine rich element binding protein B"
location: "7p13"
module: 16
arm: "+"
pooled_cpm: 62.07
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# PURB

*purine rich element binding protein B* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.80× (z +10.7, q 3e-24, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.796× (z -4.3, q 0.007, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0908×; ⚠ toxic; cell-cycle shift, explains ~26% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (AsPC-1 0.0770×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.431×; ⚠ cell-cycle shift, explains ~17% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUG1]] (+0.76, fdr 7e-06), [[C6orf120]] (+0.72, fdr 7e-06), [[RBM15B]] (+0.68, fdr 7e-06); moves opposite to [[SGK3]] (-0.69, fdr 7e-06), [[PRKRA]] (-0.66, fdr 1e-05), [[ELP2]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +10.7 | 3e-24 | 43/48 (BT-474, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.79×** | +9.9 | 1e-20 | 40/49 (LoVo, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +8.8 | 3e-16 | 34/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +8.6 | 1e-15 | 37/45 (SK-MEL-2, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +7.8 | 6e-13 | 37/49 (COLO 205, RKO, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.14×** | +7.3 | 2e-11 | 34/48 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +7.1 | 9e-11 | 33/43 (NCI-H1573, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +6.9 | 4e-10 | 29/48 (A-172, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.3 | 2e-08 | 31/48 (A498, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.0 | 1e-07 | 26/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +5.0 | 2e-05 | 29/48 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +4.9 | 4e-05 | 25/48 (A-427, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.29×** | +4.6 | 2e-04 | 23/48 (SNU-1, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.5 | 2e-04 | 25/47 (NCI-H1573, SW1417, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +4.4 | 4e-04 | 21/48 (SNU-1, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.020 | 17/47 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.030 | 15/48 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.035 | 12/48 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.044 | 10/49 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.047 | 12/48 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.047 | 9/49 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.047 | 16/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.12× | +3.0 | 0.061 | 7/48 (H4, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7112.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0908×; ⚠ toxic; cell-cycle shift, explains ~26% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (AsPC-1 0.0770×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.431×; ⚠ cell-cycle shift, explains ~17% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.796×** | -4.3 | 0.007 | 25/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.787×** | -4.2 | 0.007 | 23/48 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.805×** | -4.0 | 0.010 | 22/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.700×** | -3.5 | 0.076 | 16/37 (AsPC-1, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.838× | -3.3 | 0.10 | 18/48 (SW 1088, LOX-IMVI, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.835× | -3.2 | 0.11 | 17/48 (LOX-IMVI, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 124 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.39× (z +10.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 81.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.9) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 29.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 67.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.88× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 97.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.6) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +9.1) | — |
| [[A498 (line)]] | wt | 80.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.1) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[AsPC-1 (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0770× (z -11.3) ⚠ toxic |
| [[BT-474 (line)]] | alt | 93.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.07× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 87.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.98× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0908× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 47.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.9) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[HS-578T (line)]] | alt | 48.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +9.8) | — |
| [[LoVo (line)]] | wt | 90.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.40× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 50.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.3) ⚠ cell-cycle shift, explains ~17% of this change |
| [[NCI-H1573 (line)]] | alt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 31.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 96.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 55.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +8.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 53.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 49.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.2) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[SW480 (line)]] | alt | 66.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.64× (z +8.5) | — |
| [[A-427 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 98.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUG1]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[C6orf120]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[RBM15B]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[ZNF655]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[TASOR]] | +0.67 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[LINC00667]] | +0.67 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[ZFP41]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.66 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[NORAD]] | +0.65 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[EIF4G1]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SSU72]] | +0.65 | +0.57 / +0.61 | both halves | 9e-06 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGK3]] | -0.69 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[PRKRA]] | -0.66 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[ELP2]] | -0.66 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[CRY2]] | -0.65 | -0.58 / -0.63 | both halves | 8e-06 |  |
| [[ABCD4]] | -0.64 | -0.77 / -0.47 | both halves | 2e-05 |  |
| [[SRP54-AS1]] | -0.63 | -0.67 / -0.58 | both halves | 8e-06 |  |
| [[CC2D1A]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ABHD18]] | -0.62 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[SCAI]] | -0.61 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[TUBE1]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[VDAC3]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[ETFDH]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises PURB's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-37.4, 16.2); signed map (-1.8, -29.6). **Vector** length 116, 31.0% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +10.5 | +9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.2 | +10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.3 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +3.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | -3.9 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.9 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | purine rich element binding protein B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,876,299-44,885,530 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PURBETA |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Purine rich element binding protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QR8](https://www.uniprot.org/uniprotkb/Q96QR8) (Transcriptional regulator protein Pur-beta):

> Transcriptional regulator which can act as an activator or a repressor. Represses the transcription of ACTA2 in fibroblasts and smooth muscle cells via its ability to interact with the purine-rich strand of a MCAT- containing element in the 5' flanking region of the gene. Represses the transcription of MYOCD, capable of repressing all isoforms of MYOCD but the magnitude of the repressive effects is most notable for the SMC- specific isoforms. Promotes hepatic glucose production by activating …

**Summary**, from NCBI Gene [5814](https://www.ncbi.nlm.nih.gov/gene/5814):

> This gene product is a sequence-specific, single-stranded DNA-binding protein. It binds preferentially to the single strand of the purine-rich element termed PUR, which is present at origins of replication and in gene flanking regions in a variety of eukaryotes from yeasts through humans. Thus, it is implicated in the control of both DNA replication and transcription. Deletion of this gene has been associated with myelodysplastic syndrome and acute myelogenous leukemia. [provided by RefSeq, Jul …

**Accessions** — [HGNC:9702](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9702) · Entrez [5814](https://www.ncbi.nlm.nih.gov/gene/5814) · UniProt [Q96QR8](https://www.uniprot.org/uniprotkb/Q96QR8) · Ensembl [ENSG00000146676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146676)

## Data

Gene col 7112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7112); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7112]; `tensor/DDL_lfc|DDL_z.npy` [7112]; `embed/gene_vectors.npy` [7112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7112 or target_col == 7112). Every well: [[PURB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PURB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
