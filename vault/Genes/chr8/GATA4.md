---
symbol: "GATA4"
type: "gene"
col: 5881
ensembl_id: "ENSG00000136574"
name: "GATA binding protein 4"
location: "8p23.1"
module: 146
arm: "+"
pooled_cpm: 8.28
n_lines_expressing: 24
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# GATA4

*GATA binding protein 4* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.81× (z +15.9, q 0e+00, up in 16 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.0845×, Panc 03.27 0.133×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.329×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.259×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.285×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.484×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP64]] (+0.63, fdr 1e-05), [[LRP5L]] (+0.61, fdr 2e-05), [[EEF2K]] (+0.58, fdr 1e-05); moves opposite to [[ZNF655]] (-0.62, fdr 1e-05), [[TRIP12]] (-0.57, fdr 2e-05), [[LINC00342]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PAX2]] → it (grade C ⚠); 2 go from it, the strongest it → [[KPNA4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5881.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +15.9 | 0e+00 | 16/21 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +8.4 | 2e-14 | 9/20 (PANC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +8.0 | 2e-13 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.09×** | +8.0 | 2e-13 | 14/21 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +7.7 | 1e-12 | 14/21 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +7.4 | 1e-11 | 12/21 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +6.3 | 2e-08 | 9/22 (RKO, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +6.0 | 2e-07 | 13/20 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.8 | 5e-07 | 9/18 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +5.7 | 7e-07 | 9/21 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.6 | 1e-06 | 9/20 (H4, KATO III, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +5.0 | 3e-05 | 17/21 (A-172, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.32×** | +4.8 | 7e-05 | 9/17 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.3 | 6e-04 | 2/19 (PANC-1, HepG2/C3A) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.0 | 0.003 | 7/21 (RKO, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.016 | 6/21 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.016 | 9/21 (PANC-1, KATO III, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +3.4 | 0.016 | 10/22 (HepG2/C3A, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.025 | 13/22 (RKO, AsPC-1, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.025 | 2/21 (A-172, NCI-H23) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.030 | 5/21 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5881.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.0845×, Panc 03.27 0.133×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.329×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.259×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.285×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.484×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Larotrectinib (drug)]] 5 µM |  | 0.791× | -3.6 | 0.16 | 9/22 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.736× | -3.2 | 0.36 | 8/21 (NCI-H23, SW 900, …) | top dose only | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5881. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 32.4 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.2) |
| [[KATO III (line)]] | alt | 39.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0845× (z -16.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 32.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.484× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 5.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[NCI-H2030 (line)]] | alt | 5.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -9.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -12.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 27.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.184× (z -9.4) ⚠ toxic |
| [[A498 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.890 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.764 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.654 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5881), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP64]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[LRP5L]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[EEF2K]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[BCL7A]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ACVR1B]] | +0.57 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[MALSU1]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ATP7B]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[NOD1]] | +0.56 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[EPB41L4B]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[HDHD5]] | +0.55 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[MRPL34]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[UBE2O]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | -0.62 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.57 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[LINC00342]] | -0.55 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[MSRA]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[DDX5]] | -0.53 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[SDCBP2-AS1]] | -0.53 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[SSUH2]] | -0.51 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[APPAT]] | -0.51 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[DBNL]] | -0.50 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[NEK10]] | -0.50 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[CHMP3]] | -0.50 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[RNF32-AS1]] | -0.50 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAX2]] | C | PAX2 activity raises GATA4's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.14× lower at baseline in the lines without PAX2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2; co-absent with the target |
| [[SSUH2]] | C | SSUH2 activity lowers GATA4's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 6.77× higher at baseline in the lines without SSUH2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KPNA4]] | B | GATA4 activity raises KPNA4's level | lines that do not express GATA4 (26) vs lines expressing it (24) | 1.24× lower at baseline in the lines without GATA4 | 0.050 | ⚠ within organs, on part of the lines; also absent: PIEZO2, TAFA5, ZNF667 |
| [[PAX2]] | C | GATA4 activity raises PAX2's level | lines that do not express GATA4 (26) vs lines expressing it (24) | 1.49× lower at baseline in the lines without GATA4 | 0.033 | ⚠ within organs, on part of the lines; also absent: PIEZO2, TAFA5, ZNF667; co-absent with the target |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.0, -6.1); signed map (-40.0, 1.7). **Vector** length 45.1, 9.42% of its response variance represented; |z| ≥ 3 in 485 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +15.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +6.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.1 | +6.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +5.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | GATA binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:11,676,959-11,760,002 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | GATA zinc finger domain containing |
| Reactome | 14 pathways, smallest: Formation of lateral plate mesoderm; Transcriptional regulation of testis differentiation; Physiological factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P43694](https://www.uniprot.org/uniprotkb/P43694) (Transcription factor GATA-4):

> Transcriptional activator that binds to the consensus sequence 5'-AGATAG-3' and plays a key role in cardiac development and function. In cooperation with TBX5, it binds to cardiac super-enhancers and promotes cardiomyocyte gene expression, while it down-regulates endocardial and endothelial gene expression. Involved in bone morphogenetic protein (BMP)-mediated induction of cardiac-specific gene expression. Binds to BMP response element (BMPRE) DNA sequences within cardiac activating regions (By …

**Summary**, from NCBI Gene [2626](https://www.ncbi.nlm.nih.gov/gene/2626):

> This gene encodes a member of the GATA family of zinc-finger transcription factors. Members of this family recognize the GATA motif which is present in the promoters of many genes. This protein is thought to regulate genes involved in embryogenesis and in myocardial differentiation and function, and is necessary for normal testicular development. Mutations in this gene have been associated with cardiac septal defects. Additionally, alterations in gene expression have been associated with …

**Accessions** — [HGNC:4173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4173) · Entrez [2626](https://www.ncbi.nlm.nih.gov/gene/2626) · UniProt [P43694](https://www.uniprot.org/uniprotkb/P43694) · Ensembl [ENSG00000136574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136574)

## Data

Gene col 5881: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5881); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5881, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5881]; `tensor/DDL_lfc|DDL_z.npy` [5881]; `embed/gene_vectors.npy` [5881]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5881 or target_col == 5881). Every well: [[GATA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
