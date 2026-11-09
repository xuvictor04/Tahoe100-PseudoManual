---
symbol: "TMPRSS5"
type: "gene"
col: 9342
ensembl_id: "ENSG00000166682"
name: "transmembrane serine protease 5"
location: "11q23.2"
module: 14
arm: "+"
pooled_cpm: 4.32
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TMPRSS5

*transmembrane serine protease 5* — 11q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.16× (z +12.2, q 1e-31, up in 20 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.309× (z -12.7, q 2e-34, down in 33 of 40 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.526× (z -7.3, q 6e-11, down in 20 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX16-NPEPL1]] (+0.62, fdr 1e-05), [[MKRN5P]] (+0.61, fdr 1e-05), [[APTX]] (+0.58, fdr 3e-05); moves opposite to [[BHLHE41]] (-0.57, fdr 2e-05), [[ZNF217]] (-0.55, fdr 1e-05), [[POGZ]] (-0.54, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +12.2 | 1e-31 | 20/32 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +7.9 | 7e-13 | 15/29 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.58×** | +7.2 | 1e-10 | 12/43 (SW480, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +6.5 | 1e-08 | 14/34 (NCI-H460, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +5.9 | 3e-07 | 15/45 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +5.8 | 7e-07 | 10/44 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.62×** | +5.4 | 6e-06 | 8/44 (NCI-H2347, SW1417, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.53×** | +4.5 | 5e-04 | 9/41 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.49×** | +4.3 | 0.001 | 2/13 (NCI-H460, HOP62) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.46×** | +4.2 | 0.001 | 8/44 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.45×** | +4.1 | 0.002 | 4/43 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.008 | 9/41 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.39×** | +3.7 | 0.011 | 3/44 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.034 | 4/27 (HCT15, HT-29, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.73×** | +3.2 | 0.048 | 3/40 (PANC-1, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.061 | 4/44 (C-33 A, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9342.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.309×** | -12.7 | 2e-34 | 33/40 (KATO III, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.488×** | -11.4 | 7e-28 | 28/35 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.478×** | -8.3 | 2e-14 | 23/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.526×** | -7.3 | 6e-11 | 20/43 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.615×** | -5.5 | 4e-06 | 16/35 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.648×** | -4.9 | 9e-05 | 16/43 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.666×** | -4.6 | 3e-04 | 11/44 (PANC-1, SW 900, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.676×** | -4.4 | 7e-04 | 12/43 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Atazanavir (sulfate) (drug)]] 0.5 µM |  | **0.690×** | -4.2 | 0.002 | 13/40 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.729×** | -3.4 | 0.032 | 8/44 (SW48, C32, …) | top dose only | plate-row cell shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.563×** | -3.4 | 0.036 | 11/38 (KATO III, HCT15, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.575×** | -3.3 | 0.051 | 4/27 (NCI-H460, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.744×** | -3.2 | 0.051 | 5/43 (KATO III, RKO, …) | top dose only |  |
| [[NG25 (drug)]] 0.05 µM |  | **0.740×** | -3.2 | 0.051 | 8/41 (SW480, A549, …) | inconsistent across doses |  |
| [[Adenine (drug)]] 0.5 µM |  | **0.765×** | -3.0 | 0.090 | 7/44 (CHP-212, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[palbociclib (drug)]] 0.05 µM |  | **0.755×** | -3.0 | 0.094 | 8/41 (hTERT-HPNE, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.82 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 50.1 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0724× (z -22.8) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -14.6) |
| [[PANC-1 (line)]] | alt | 6.47 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.6) ⚠ cell-cycle shift, explains ~77% of this change |
| [[SW480 (line)]] | alt | 7.10 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -15.5) ⚠ cell-cycle shift, explains ~77% of this change |
| [[HEC-1-A (line)]] | alt | 5.77 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -9.3) ⚠ cell-cycle shift, explains ~77% of this change |
| [[NCI-H460 (line)]] | wt | 2.50 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -8.8) ⚠ cell-cycle shift, explains ~77% of this change |
| [[A-172 (line)]] | wt | 2.50 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -9.6) ⚠ cell-cycle shift, explains ~77% of this change |
| [[C32 (line)]] | wt | 3.83 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -8.7) ⚠ cell-cycle shift, explains ~77% of this change |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0854× (z -9.4) |
| [[A-427 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX16-NPEPL1]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MKRN5P]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[APTX]] | +0.58 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[PPP1R32]] | +0.58 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[CDC26]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ADPGK]] | +0.57 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[GLUD1P3]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[NPIPB11]] | +0.56 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PPHLN1]] | +0.56 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[TSNAX-DISC1]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[DRD4]] | +0.55 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NBR2]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BHLHE41]] | -0.57 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[ZNF217]] | -0.55 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[POGZ]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SFR1]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[VEZF1]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ARL4A]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[DHRS2]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[SNAPIN]] | -0.52 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[NALCN]] | -0.52 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[ONECUT2]] | -0.51 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[MAP3K14]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[TIGD2]] | -0.51 | -0.32 / -0.58 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction -0.393). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.7, -15.9); signed map (4.9, 4.4). **Vector** length 53.9, 6.51% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | +2.6 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.6 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +2.6 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | -2.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.3 | -12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -4.2 | -11.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -3.2 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane serine protease 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.2 — chr11:113,687,547-113,706,373 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC141886, MGC148044 |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing; Type II transmembrane serine proteases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3S3](https://www.uniprot.org/uniprotkb/Q9H3S3) (Transmembrane protease serine 5):

> May play a role in hearing.

**Summary**, from NCBI Gene [80975](https://www.ncbi.nlm.nih.gov/gene/80975):

> This gene encodes a protein that belongs to the serine protease family. Serine proteases are known to be involved in many physiological and pathological processes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:14908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14908) · Entrez [80975](https://www.ncbi.nlm.nih.gov/gene/80975) · UniProt [Q9H3S3](https://www.uniprot.org/uniprotkb/Q9H3S3) · Ensembl [ENSG00000166682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166682)

## Data

Gene col 9342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9342); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9342]; `tensor/DDL_lfc|DDL_z.npy` [9342]; `embed/gene_vectors.npy` [9342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9342 or target_col == 9342). Every well: [[TMPRSS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMPRSS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
