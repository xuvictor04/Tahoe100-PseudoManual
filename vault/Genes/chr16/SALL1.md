---
symbol: "SALL1"
type: "gene"
col: 2367
ensembl_id: "ENSG00000103449"
name: "spalt like transcription factor 1"
location: "16q12.1"
module: 202
arm: "+"
pooled_cpm: 3.91
n_lines_expressing: 20
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# SALL1

*spalt like transcription factor 1* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.81× (z +15.3, q 0e+00, up in 6 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.40× (z +9.8, q 1e-20, up in 12 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.576× (z -4.5, q 0.005, down in 9 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.231×); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.237×); [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.0547×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL7R]] (+0.63, fdr 1e-05), [[OFCC1]] (+0.60, fdr 2e-05), [[NANOS3]] (+0.59, fdr 1e-05); moves opposite to [[SCAI]] (-0.56, fdr 2e-05), [[GTF2H2B]] (-0.53, fdr 8e-05), [[DUXAP10]] (-0.52, fdr 3e-05).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ITGBL1]] → it (grade C ⚠); 5 go from it, the strongest it → [[TRIM69]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2367.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.81×** | +15.3 | 0e+00 | 6/13 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.66×** | +13.3 | 1e-37 | 2/9 (NCI-H460, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.40×** | +9.8 | 1e-20 | 12/16 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.73×** | +9.7 | 5e-20 | 5/10 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.64×** | +7.7 | 2e-12 | 9/15 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +7.3 | 3e-11 | 7/15 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +7.3 | 3e-11 | 4/12 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.01×** | +6.3 | 3e-08 | 0/11 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +6.2 | 3e-08 | 2/15 (NCI-H460, NCI-H1573) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +5.8 | 3e-07 | 5/16 (A-172, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.09×** | +5.6 | 1e-06 | 13/18 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.96×** | +5.3 | 5e-06 | 1/13 (HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.1 | 1e-05 | 5/17 (A-172, NCI-H2030, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.0 | 2e-05 | 1/15 (SNU-423) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +4.6 | 2e-04 | 3/17 (NCI-H1573, H4, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.66×** | +4.0 | 0.002 | 0/15 | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +3.8 | 0.004 | 5/15 (NCI-H1573, A498, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.009 | 12/18 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.022 | 1/15 (A-427) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.77×** | +3.2 | 0.033 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.53×** | +3.2 | 0.036 | 3/17 (RPMI-7951, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.066 | 4/15 (NCI-H1573, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.069 | 1/15 (RPMI-7951) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2367.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.231×); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.237×); [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.0547×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.576×** | -4.5 | 0.005 | 9/18 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.672× | -3.2 | 0.36 | 1/16 (SNU-423) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.4 | 6 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +17.0) | [[Panobinostat (drug)]] 5 µM 0.178× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.231× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 8.35 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +14.7) | — |
| [[A-172 (line)]] | wt | 18.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.326× (z -8.5) |
| [[H4 (line)]] | wt | 16.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0547× (z -8.5) |
| [[A-427 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.209 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.980 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.280 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.306 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.215 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL7R]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[OFCC1]] | +0.60 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[NANOS3]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[NR2F1-AS1]] | +0.59 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[DEDD]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SCN3A]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ZNF385D]] | +0.58 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[LINC00702]] | +0.58 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[C1QTNF1]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[SYNPO]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SOCS2-AS1]] | +0.57 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[SOCS2]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAI]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[GTF2H2B]] | -0.53 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[DUXAP10]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[VDAC3]] | -0.52 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ABCD4]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[CRYZL1]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[HEBP1]] | -0.51 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[SGK3]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[FBXO42]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[APPL1]] | -0.49 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[PPP1R12B]] | -0.48 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGBL1]] | C | ITGBL1 activity raises SALL1's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 2.80× lower at baseline in the lines without ITGBL1 | 0.055 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[SYNPO]] | C | SYNPO activity raises SALL1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.78× lower at baseline in the lines without SYNPO | 0.070 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent; co-absent with the target |
| [[SUCNR1]] | C | SUCNR1 activity raises SALL1's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 3.46× lower at baseline in the lines without SUCNR1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM69]] | B | SALL1 activity raises TRIM69's level | lines that do not express SALL1 (30) vs lines expressing it (20) | 1.28× lower at baseline in the lines without SALL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LINC01411, GUCY1B1 |
| [[APCDD1L-DT]] | C | SALL1 activity raises APCDD1L-DT's level | lines that do not express SALL1 (30) vs lines expressing it (20) | 3.29× lower at baseline in the lines without SALL1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LINC01411, GUCY1B1; co-absent with the target |
| [[COL5A3]] | C | SALL1 activity raises COL5A3's level | lines that do not express SALL1 (30) vs lines expressing it (20) | 3.19× lower at baseline in the lines without SALL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LINC01411, GUCY1B1; co-absent with the target |
| [[GREM1]] | C | SALL1 activity raises GREM1's level | lines that do not express SALL1 (30) vs lines expressing it (20) | 2.70× lower at baseline in the lines without SALL1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LINC01411, GUCY1B1; co-absent with the target |
| [[ZNF469]] | C | SALL1 activity raises ZNF469's level | lines that do not express SALL1 (30) vs lines expressing it (20) | 2.93× lower at baseline in the lines without SALL1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LINC01411, GUCY1B1; co-absent with the target |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.8, 18.2); signed map (27.3, 8.4). **Vector** length 42.5, 10.9% of its response variance represented; |z| ≥ 3 in 333 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +15.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.2 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | spalt like transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:51,135,982-51,152,334 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hsal1, ZNF794; previously TBS |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Reactome | 4 pathways, smallest: POU5F1 (OCT4), SOX2, NANOG activate genes related to proliferation; Formation of the ureteric bud; Transcriptional regulation of pluripotent stem cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSC2](https://www.uniprot.org/uniprotkb/Q9NSC2) (Sal-like protein 1):

> Transcriptional repressor involved in organogenesis. Plays an essential role in ureteric bud invasion during kidney development.

**Summary**, from NCBI Gene [6299](https://www.ncbi.nlm.nih.gov/gene/6299):

> The protein encoded by this gene is a zinc finger transcriptional repressor and may be part of the NuRD histone deacetylase complex (HDAC). Defects in this gene are a cause of Townes-Brocks syndrome (TBS) as well as bronchio-oto-renal syndrome (BOR). Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10524) · Entrez [6299](https://www.ncbi.nlm.nih.gov/gene/6299) · UniProt [Q9NSC2](https://www.uniprot.org/uniprotkb/Q9NSC2) · Ensembl [ENSG00000103449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103449)

## Data

Gene col 2367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2367); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2367]; `tensor/DDL_lfc|DDL_z.npy` [2367]; `embed/gene_vectors.npy` [2367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2367 or target_col == 2367). Every well: [[SALL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SALL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
