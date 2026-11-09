---
symbol: "ABCC9"
type: "gene"
col: 918
ensembl_id: "ENSG00000069431"
name: "ATP binding cassette subfamily C member 9"
location: "12p12.1"
module: 19
arm: "+"
pooled_cpm: 4.25
n_lines_expressing: 22
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 17
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ABCC9

*ATP binding cassette subfamily C member 9* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.02× (z +17.9, q 0e+00, up in 12 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H460 0.166×, J82 0.103×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.0982×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.168×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCN3A]] (+0.71, fdr 7e-06), [[NLGN4Y]] (+0.69, fdr 7e-06), [[CPED1]] (+0.67, fdr 7e-06); moves opposite to [[SDHAP1]] (-0.56, fdr 2e-05), [[ABHD12]] (-0.54, fdr 4e-05), [[OXNAD1]] (-0.52, fdr 4e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 17 go from it, the strongest it → [[LY96]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.02×** | +17.9 | 0e+00 | 12/14 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.53×** | +12.7 | 1e-34 | 2/4 (NCI-H2347, J82) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.72×** | +11.9 | 1e-30 | 6/12 (SW 900, A498, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.90×** | +11.9 | 1e-30 | 0/5 | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.21×** | +10.6 | 3e-24 | 10/13 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +10.4 | 2e-23 | 4/14 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.09×** | +6.5 | 8e-09 | 12/15 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.1 | 9e-08 | 4/14 (hTERT-HPNE, SW1417, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.93×** | +6.0 | 1e-07 | 6/15 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.2 | 1e-05 | 4/16 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.1 | 2e-05 | 3/9 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.86×** | +5.0 | 3e-05 | 9/15 (NCI-H2347, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +4.9 | 4e-05 | 7/15 (NCI-H2347, LOX-IMVI, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +4.4 | 5e-04 | 10/15 (NCI-H2347, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +4.2 | 0.001 | 1/8 (SNU-423) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.007 | 2/14 (SW480, HOP62) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.51×** | +3.5 | 0.015 | 1/12 (hTERT-HPNE) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.031 | 3/12 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.031 | 6/15 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Estrone sulfate (potassium) (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.031 | 2/15 (hTERT-HPNE, SW480) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.032 | 4/13 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H460 0.166×, J82 0.103×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.0982×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.168×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 8.17 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +13.7) | — |
| [[NCI-H460 (line)]] | wt | 35.9 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0982× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.166× (z -11.4) |
| [[A-172 (line)]] | wt | 1.97 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.2× (z +12.9) | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0911× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.103× (z -9.1) |
| [[SW 900 (line)]] | alt | 4.49 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 1.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +11.6) | — |
| [[HS-578T (line)]] | alt | 2.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 7.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 3.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +12.4) | — |
| [[SW480 (line)]] | alt | 1.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +8.8) | — |
| [[A-427 (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.936 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.830 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.866 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.956 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.837 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.813 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.943 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCN3A]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 | pathway: Cardiac conduction |
| [[NLGN4Y]] | +0.69 | +0.72 / +0.58 | both halves | 7e-06 | pathway: Neuronal System |
| [[CPED1]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[MARCOL]] | +0.65 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[IL7R]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SLAMF7]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ALPK2]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[SOX11]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TLR6]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[SHISAL1]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[IGSF1]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[LINC01828]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ABHD12]] | -0.54 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[OXNAD1]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[GMCL1]] | -0.51 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[SDHAP2]] | -0.51 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[RAB40B]] | -0.51 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[SMARCD2]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ABCC9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TRIP6]] | B | TRIP6 activity raises ABCC9's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.62× lower at baseline in the lines without TRIP6 | 0.088 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[DGKI]] | C | DGKI activity raises ABCC9's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without DGKI | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[SCN3A]] | C | SCN3A activity raises ABCC9's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without SCN3A | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises ABCC9's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.86× lower at baseline in the lines without NLGN4Y | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[CCDC80]] | C | CCDC80 activity raises ABCC9's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 1.96× lower at baseline in the lines without CCDC80 | 0.073 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises ABCC9's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without ALPK2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[DNAH11]] | C | DNAH11 activity raises ABCC9's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 1.97× lower at baseline in the lines without DNAH11 | 0.096 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 5, C 12. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LY96]] | B | ABCC9 activity raises LY96's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 2.31× lower at baseline in the lines without ABCC9 | 0.050 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent |
| [[TRIP6]] | B | ABCC9 activity raises TRIP6's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without ABCC9 | 0.062 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent |
| [[LINC01828]] | B | ABCC9 activity strengthens LINC01828's drug response | lines that do not express ABCC9 (14) vs lines expressing it (15) | the lines without ABCC9 respond 0.37× as strongly (z diff +1.77); strongest at Homoharringtonine 5 µM: 1.42x vs 5.64x (z diff +6.0) | 0.071 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SLC6A7]] | B | ABCC9 activity raises SLC6A7's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 1.44× lower at baseline in the lines without ABCC9 | 0.074 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | ABCC9 activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express ABCC9 (28) vs lines expressing it (20) | the lines without ABCC9: 0.83× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent |
| [[CCDC80]] | C | ABCC9 activity raises CCDC80's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 4.96× lower at baseline in the lines without ABCC9 | 0.003 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[IL7R]] | C | ABCC9 activity raises IL7R's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 4.69× lower at baseline in the lines without ABCC9 | 0.007 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[FGF5]] | C | ABCC9 activity raises FGF5's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 3.78× lower at baseline in the lines without ABCC9 | 0.024 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[LY6K]] | C | ABCC9 activity raises LY6K's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 3.32× lower at baseline in the lines without ABCC9 | 0.027 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[DOCK10]] | C | ABCC9 activity raises DOCK10's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 4.27× lower at baseline in the lines without ABCC9 | 0.056 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[DNAH11]] | C | ABCC9 activity raises DNAH11's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 3.48× lower at baseline in the lines without ABCC9 | 0.059 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[LINC02241]] | C | ABCC9 activity raises LINC02241's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 2.25× lower at baseline in the lines without ABCC9 | 0.065 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.1, 25.9); signed map (41.4, 27.1). **Vector** length 47.6, 12.9% of its response variance represented; |z| ≥ 3 in 417 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +17.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily C member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:21,797,389-21,942,543 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SUR2, CMD1O |
| Gene groups (HGNC) | ATP binding cassette subfamily C; ATP-sensitive potassium channel subunits |
| Reactome | 10 pathways, smallest: Inwardly rectifying K+ channels; Ion homeostasis; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [O60706](https://www.uniprot.org/uniprotkb/O60706) (ATP-binding cassette sub-family C member 9):

> Subunit of ATP-sensitive potassium channels (KATP). Can form cardiac and smooth muscle-type KATP channels with KCNJ11. KCNJ11 forms the channel pore while ABCC9 is required for activation and regulation. Can form a sulfonylurea-sensitive but ATP-insensitive potassium channel with KCNJ8 (By similarity).

**Summary**, from NCBI Gene [10060](https://www.ncbi.nlm.nih.gov/gene/10060):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MRP subfamily which is involved in multi-drug resistance. This protein is thought to form ATP-sensitive potassium channels in cardiac, skeletal, and vascular and …

**Accessions** — [HGNC:60](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:60) · Entrez [10060](https://www.ncbi.nlm.nih.gov/gene/10060) · UniProt [O60706](https://www.uniprot.org/uniprotkb/O60706) · Ensembl [ENSG00000069431](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069431)

## Data

Gene col 918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 918); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 918]; `tensor/DDL_lfc|DDL_z.npy` [918]; `embed/gene_vectors.npy` [918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 918 or target_col == 918). Every well: [[ABCC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
