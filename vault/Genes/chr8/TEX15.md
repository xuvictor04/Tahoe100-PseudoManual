---
symbol: "TEX15"
type: "gene"
col: 5482
ensembl_id: "ENSG00000133863"
name: "testis expressed 15, meiosis and synapsis associated"
location: "8p12"
module: 82
arm: "+"
pooled_cpm: 7.8
n_lines_expressing: 21
n_dd_up: 42
n_dd_down: 2
n_dd_up_clean: 25
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# TEX15

*testis expressed 15, meiosis and synapsis associated* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 11.2× (z +23.4, q 0e+00, up in 19 of 19 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 4.76× (z +21.3, q 0e+00, up in 19 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.859× (z -5.2, q 1e-04, down in 7 of 19 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ciclopirox (drug)]] 0.5 µM: 0.698× (z -3.5, q 0.088, down in 2 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (C-33 A 0.183×, Hs 766T 0.0799×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.0717×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Penfluridol (drug)]] 0.05 µM in 1 line (CHP-212 0.0412×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0752×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM108]] (+0.73, fdr 7e-06), [[MED12L]] (+0.66, fdr 7e-06), [[SYN2]] (+0.64, fdr 7e-06); moves opposite to [[LRRC27]] (-0.49, fdr 4e-05), [[ENTPD3-AS1]] (-0.49, fdr 2e-04), [[BBOF1]] (-0.49, fdr 5e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **11.2×** | +23.4 | 0e+00 | 19/19 (J82, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **9.16×** | +21.4 | 0e+00 | 19/19 (NCI-H1573, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **4.76×** | +21.3 | 0e+00 | 19/19 (NCI-H2347, C-33 A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.13×** | +19.4 | 0e+00 | 10/18 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **6.72×** | +18.4 | 0e+00 | 19/19 (NCI-H1573, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **4.10×** | +13.7 | 2e-40 | 9/14 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.94×** | +13.3 | 3e-38 | 19/19 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.91×** | +12.7 | 6e-35 | 2/6 (NCI-H2347, J82) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.45×** | +12.0 | 3e-31 | 17/19 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.72×** | +9.7 | 2e-20 | 14/19 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.90×** | +9.5 | 8e-20 | 3/9 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.47×** | +8.7 | 1e-16 | 16/19 (NCI-H2347, C-33 A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.14×** | +7.4 | 8e-12 | 13/18 (NCI-H23, SW 900, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.9 | 3e-10 | 10/19 (NCI-H23, SW 900, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.01×** | +6.7 | 7e-10 | 16/19 (A-427, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **3.67×** | +6.6 | 2e-09 | 16/18 (A498, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +6.3 | 1e-08 | 7/17 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +5.3 | 3e-06 | 9/19 (NCI-H2347, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.38×** | +4.4 | 3e-04 | 6/19 (J82, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +4.0 | 0.001 | 6/18 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.002 | 9/19 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[vincristine (drug)]] 5 µM |  | **2.13×** | +3.8 | 0.003 | 1/11 (NCI-H2030) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5482.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (C-33 A 0.183×, Hs 766T 0.0799×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.0717×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Penfluridol (drug)]] 0.05 µM in 1 line (CHP-212 0.0412×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0752×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.859× | -5.2 | 1e-04 | 7/19 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.674×** | -3.7 | 0.063 | 6/18 (CHP-212, NCI-H23, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | **0.698×** | -3.5 | 0.088 | 2/19 (NCI-H661, HOP62) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.802× | -3.0 | 0.30 | 4/19 (NCI-H2030, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.10 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 77.4 | 1 | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.04× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.183× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[NCI-H2347 (line)]] | alt | 57.6 | 5 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.88× (z +12.3) | — |
| [[A498 (line)]] | wt | 2.07 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 34.7× (z +11.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 10.6× (z +10.4) | — |
| [[J82 (line)]] | alt | 8.69 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 13.7× (z +11.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 5.60× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 5.65 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 26.8× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0752× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 46.8 | 3 (2 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 3.21× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.0717× (z -23.3) |
| [[A-427 (line)]] | wt | 95.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.29× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H2030 (line)]] | alt | 2.41 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 10.1× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 4.76 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 8.92× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 1 | — | [[Penfluridol (drug)]] 0.05 µM 0.0412× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 2.37 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.28× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 1.95 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 24.0× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 6.20 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0799× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[SW480 (line)]] | alt | 2.46 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.23× (z +10.7) | — |
| [[A-172 (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.718 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM108]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MED12L]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SYN2]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PDGFD]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[LPAR3]] | +0.60 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[GABRB3]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LHX2]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[FAM184A]] | +0.58 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[GLDC]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[RET]] | +0.56 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[FABP5]] | +0.56 | +0.37 / +0.58 | both halves | 8e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC27]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[ENTPD3-AS1]] | -0.49 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[BBOF1]] | -0.49 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[FBXL9P]] | -0.46 | -0.30 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TEX15's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.4% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[RNF152]] | B | RNF152 activity lowers TEX15's level | lines that do not express RNF152 (18) vs lines expressing it (32) | 1.59× higher at baseline in the lines without RNF152 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, SNCAIP, OR9Q1; maybe low, not absent |
| [[TLL1]] | C | TLL1 activity raises TEX15's level | lines that do not express TLL1 (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without TLL1 | 0.066 | ⚠ within organs, on part of the lines; also absent: GUCY1A1, CDH6, COL1A1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.8, 37.6); signed map (28.1, 26.1). **Vector** length 53.6, 13.3% of its response variance represented; |z| ≥ 3 in 552 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +21.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +5.7 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +5.4 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.7 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed 15, meiosis and synapsis associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:30,831,544-30,913,008 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CT42 |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 4 pathways, smallest: Meiotic recombination; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXT5](https://www.uniprot.org/uniprotkb/Q9BXT5) (Testis-expressed protein 15):

> Required during spermatogenesis for normal chromosome synapsis and meiotic recombination in germ cells. Necessary for formation of DMC1 and RAD51 foci on meiotic chromosomes, suggesting a specific role in DNA double-stranded break repair (By similarity). Essential executor of PIWIL4-piRNA pathway directed transposon DNA methylation and silencing in the male embryonic germ cells (By similarity). PIWIL4-piRNA binds to nascent transposon transcripts and interacts with TEX15, which may in turn …

**Summary**, from NCBI Gene [56154](https://www.ncbi.nlm.nih.gov/gene/56154):

> This gene encodes a protein that is required for DNA double-strand break repair, chromosome synapsis, and meiotic recombination in spermatocytes. Male mice with a knockout of the orthologous gene are viable but sterile. Loss-of-function mutations in the orthologous mouse gene cause early meiotic arrest in spermatocytes, before the mid-pachytene stage. Naturally occurring mutations in this gene are associated with nonobstructive azoospermia. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:11738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11738) · Entrez [56154](https://www.ncbi.nlm.nih.gov/gene/56154) · UniProt [Q9BXT5](https://www.uniprot.org/uniprotkb/Q9BXT5) · Ensembl [ENSG00000133863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133863)

## Data

Gene col 5482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5482); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5482]; `tensor/DDL_lfc|DDL_z.npy` [5482]; `embed/gene_vectors.npy` [5482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5482 or target_col == 5482). Every well: [[TEX15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEX15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
