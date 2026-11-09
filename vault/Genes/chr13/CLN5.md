---
symbol: "CLN5"
type: "gene"
col: 2275
ensembl_id: "ENSG00000102805"
name: "CLN5 lysosomal BMP synthase"
location: "13q22.3"
module: 94
arm: "+"
pooled_cpm: 12.49
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# CLN5

*CLN5 lysosomal BMP synthase* — 13q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.97× (z +24.7, q 0e+00, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.726× (z -5.1, q 2e-04, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 0.0866×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (Panc 03.27 0.253×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM200B]] (+0.80, fdr 7e-06), [[ZNF442]] (+0.73, fdr 7e-06), [[PHYH]] (+0.71, fdr 1e-05); moves opposite to [[EPS15L1]] (-0.64, fdr 1e-05), [[GNB1L]] (-0.64, fdr 1e-05), [[RNF216]] (-0.62, fdr 8e-05).
> It is in [[Module 094]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.97×** | +24.7 | 0e+00 | 37/46 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.34×** | +19.2 | 0e+00 | 42/48 (HT-29, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.80×** | +15.9 | 0e+00 | 36/47 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.17×** | +12.4 | 3e-33 | 33/46 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +12.0 | 3e-31 | 25/32 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +11.2 | 4e-27 | 29/41 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.93×** | +10.5 | 4e-24 | 34/48 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.8 | 7e-21 | 22/35 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +9.7 | 1e-20 | 31/46 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.78×** | +9.3 | 1e-18 | 36/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +7.4 | 1e-11 | 14/26 (AsPC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.47×** | +6.2 | 4e-08 | 25/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.7 | 5e-07 | 21/46 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +5.3 | 4e-06 | 20/43 (RPMI-7951, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 2e-05 | 17/46 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 4e-05 | 14/47 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.7 | 1e-04 | 16/47 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.6 | 1e-04 | 12/48 (J82, A-172, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.012 | 5/45 (Hs 766T, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.4 | 0.016 | 5/48 (Hs 766T, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2275.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 0.0866×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (Panc 03.27 0.253×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.726×** | -5.1 | 2e-04 | 18/47 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.826× | -3.1 | 0.60 | 13/47 (Panc 03.27, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +18.5) | — |
| [[HEC-1-A (line)]] | alt | 13.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +15.4) | — |
| [[J82 (line)]] | alt | 18.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +16.5) | — |
| [[KATO III (line)]] | alt | 14.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +15.9) | — |
| [[HT-29 (line)]] | alt | 12.0 | 2 | 0 | [[Selinexor (drug)]] 5 µM 4.29× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 25.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 14.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 9.59 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +10.8) | — |
| [[SW480 (line)]] | alt | 18.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.7) | — |
| [[A498 (line)]] | wt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +8.8) | — |
| [[LoVo (line)]] | wt | 8.87 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.27× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 9.16 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.63× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 9.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 9.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +13.8) | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0866× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[SW48 (line)]] | wt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +9.3) | — |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200B]] | +0.80 | +0.83 / +0.68 | both halves | 7e-06 |  |
| [[ZNF442]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[PHYH]] | +0.71 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[ETFRF1]] | +0.71 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[ZNF627]] | +0.70 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[TRAM2-AS1]] | +0.70 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.69 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ZNF44]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[PLEKHF2]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[OSGIN2]] | +0.68 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ZNF563]] | +0.68 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[SLC43A2]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS15L1]] | -0.64 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[GNB1L]] | -0.64 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[RNF216]] | -0.62 | -0.70 / -0.37 | both halves | 8e-05 |  |
| [[DGKD]] | -0.61 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[LPCAT1]] | -0.60 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[HIRA]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[TBC1D24]] | -0.58 | -0.64 / -0.34 | both halves | 1e-04 |  |
| [[PRIM2]] | -0.57 | -0.61 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.7, 22.9); signed map (17.0, -17.0). **Vector** length 87.6, 17.4% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +12.5 | +19.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +24.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.9 | +15.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.7 | +10.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +12.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.4 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +3.1 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Mifepristone (drug)]] 0.5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | CLN5 lysosomal BMP synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.3 — chr13:76,990,660-77,019,143 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Thioester hydrolases |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [O75503](https://www.uniprot.org/uniprotkb/O75503) (Bis(monoacylglycero)phosphate synthase CLN5):

> [Bis(monoacylglycero)phosphate synthase CLN5, secreted form]: Catalyzes the synthesis of bis(monoacylglycero)phosphate (BMP) via transacylation of 2 molecules of lysophosphatidylglycerol (LPG). BMP also known as lysobisphosphatidic acid plays a key role in the formation of intraluminal vesicles and in maintaining intracellular cholesterol homeostasis. Can use only LPG as the exclusive lysophospholipid acyl donor for base exchange and displays BMP synthase activity towards various LPGs (LPG …

**Summary**, from NCBI Gene [1203](https://www.ncbi.nlm.nih.gov/gene/1203):

> This gene is one of eight which have been associated with neuronal ceroid lipofuscinoses (NCL). Also referred to as Batten disease, NCL comprises a class of autosomal recessive, neurodegenerative disorders affecting children. The genes responsible likely encode proteins involved in the degradation of post-translationally modified proteins in lysosomes. The primary defect in NCL disorders is thought to be associated with lysosomal storage function.[provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:2076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2076) · Entrez [1203](https://www.ncbi.nlm.nih.gov/gene/1203) · UniProt [O75503](https://www.uniprot.org/uniprotkb/O75503) · Ensembl [ENSG00000102805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102805)

## Data

Gene col 2275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2275); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2275]; `tensor/DDL_lfc|DDL_z.npy` [2275]; `embed/gene_vectors.npy` [2275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2275 or target_col == 2275). Every well: [[CLN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
