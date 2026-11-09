---
symbol: "CHMP1B2P"
type: "gene"
col: 15914
ensembl_id: "ENSG00000278530"
name: "charged multivesicular body protein 1B2, pseudogene"
location: "Xq21.1"
module: 102
arm: "+"
pooled_cpm: 9.27
n_lines_expressing: 19
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 11
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# CHMP1B2P

*charged multivesicular body protein 1B2, pseudogene* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.43× (z +9.7, q 1e-19, up in 1 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +8.0, q 3e-13, up in 11 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.743× (z -4.8, q 8e-04, down in 14 of 17 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.470× (z -4.5, q 0.002, down in 15 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (NCI-H23 0.215×, NCI-H1573 0.131×, NCI-H1792 0.192×, SNU-423 0.139×, …; ⚠ cell-cycle shift, explains ~57% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.145×, SK-MEL-2 0.155×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.244×, SK-MEL-2 0.295×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H23 0.0916×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD6]] (+0.62, fdr 1e-05), [[LINC00648]] (+0.62, fdr 7e-06), [[LINC03046]] (+0.60, fdr 1e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 11 go from it, the strongest it → [[LINC00648]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +9.7 | 1e-19 | 1/14 (A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +8.0 | 3e-13 | 11/17 (J82, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +7.3 | 4e-11 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +6.9 | 7e-10 | 0/16 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.9 | 5e-07 | 0/17 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +5.6 | 2e-06 | 12/17 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.6 | 3e-04 | 6/17 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 0.001 | 6/17 (AN3 CA, A498, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.004 | 2/17 (J82, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.27×** | +3.8 | 0.007 | 11/17 (A498, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.037 | 0/17 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.043 | 4/17 (A-427, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.044 | 11/17 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.2 | 0.052 | 0/14 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.2 | 0.054 | 0/17 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.094 | 6/17 (A498, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15914.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (NCI-H23 0.215×, NCI-H1573 0.131×, NCI-H1792 0.192×, SNU-423 0.139×, …; ⚠ cell-cycle shift, explains ~57% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.145×, SK-MEL-2 0.155×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.244×, SK-MEL-2 0.295×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H23 0.0916×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.743×** | -4.8 | 8e-04 | 14/17 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.470×** | -4.5 | 0.002 | 15/17 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | 0.757× | -3.2 | 0.26 | 2/17 (CFPAC-1, AN3 CA) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.770× | -3.0 | 0.37 | 5/16 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 102 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -18.1) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0916× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 78.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -14.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 14.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -11.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H1573 (line)]] | alt | 30.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -16.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[AN3 CA (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0952× (z -8.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -14.0) ⚠ cell-cycle shift, explains ~57% of this change |
| [[Panc 03.27 (line)]] | alt | 6.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0558× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -13.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -13.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 0.768 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.949 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.852 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.989 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.910 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.755 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD6]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[LINC00648]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LINC03046]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ANO5]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[ADAM23]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LRRN2]] | +0.56 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[GALNT13]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LINC00470]] | +0.53 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[SCN8A]] | +0.53 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[NINL]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[HAGLR]] | +0.51 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[DOCK3]] | +0.51 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CHMP1B2P's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00648]] | C | LINC00648 activity raises CHMP1B2P's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 5.48× lower at baseline in the lines without LINC00648 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1; co-absent with the target |
| [[LINC03046]] | C | LINC03046 activity raises CHMP1B2P's level | lines that do not express LINC03046 (38) vs lines expressing it (12) | 5.19× lower at baseline in the lines without LINC03046 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, LINC00824, LINC01205; co-absent with the target |
| [[LIN28B]] | C | LIN28B activity raises CHMP1B2P's level | lines that do not express LIN28B (31) vs lines expressing it (19) | 3.76× lower at baseline in the lines without LIN28B | 0.010 | ⚠ within organs, on part of the lines; also absent: LRFN5, BARX1, KCNH7; co-absent with the target |
| [[ST8SIA6-AS1]] | C | ST8SIA6-AS1 activity raises CHMP1B2P's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 6.28× lower at baseline in the lines without ST8SIA6-AS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[NAA11]] | C | NAA11 activity raises CHMP1B2P's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 5.03× lower at baseline in the lines without NAA11 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[MIR3171HG]] | C | MIR3171HG activity raises CHMP1B2P's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 4.25× lower at baseline in the lines without MIR3171HG | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[MIR646HG]] | C | MIR646HG activity raises CHMP1B2P's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 3.69× lower at baseline in the lines without MIR646HG | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises CHMP1B2P's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 4.47× lower at baseline in the lines without EVC2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[TMEM108]] | C | TMEM108 activity raises CHMP1B2P's level | lines that do not express TMEM108 (23) vs lines expressing it (27) | 3.11× lower at baseline in the lines without TMEM108 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: TWIST1, FYB1, GATA3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00648]] | C | CHMP1B2P activity raises LINC00648's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 3.22× lower at baseline in the lines without CHMP1B2P | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[NAA11]] | C | CHMP1B2P activity raises NAA11's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 2.31× lower at baseline in the lines without CHMP1B2P | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[LINC03046]] | C | CHMP1B2P activity raises LINC03046's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 3.05× lower at baseline in the lines without CHMP1B2P | 0.030 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[ZNF208]] | C | CHMP1B2P activity raises ZNF208's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 2.10× lower at baseline in the lines without CHMP1B2P | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[L3MBTL4]] | C | CHMP1B2P activity raises L3MBTL4's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 3.84× lower at baseline in the lines without CHMP1B2P | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[LINC02616]] | C | CHMP1B2P activity raises LINC02616's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without CHMP1B2P | 0.061 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[NLGN4X]] | C | CHMP1B2P activity raises NLGN4X's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without CHMP1B2P | 0.061 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[RNF17]] | C | CHMP1B2P activity raises RNF17's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 1.81× lower at baseline in the lines without CHMP1B2P | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[MIR3171HG]] | C | CHMP1B2P activity raises MIR3171HG's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 3.36× lower at baseline in the lines without CHMP1B2P | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[LINC01446]] | C | CHMP1B2P activity raises LINC01446's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 2.78× lower at baseline in the lines without CHMP1B2P | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[GABRG2]] | C | CHMP1B2P activity raises GABRG2's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 1.89× lower at baseline in the lines without CHMP1B2P | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.504). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.2, 37.2); signed map (38.5, 40.9). **Vector** length 46.6, 12.9% of its response variance represented; |z| ≥ 3 in 347 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -1.5 | -4.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 1B2, pseudogene |
| Locus type | pseudogene |
| Location | Xq21.1 — chrX:80,272,065-80,335,227 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49380) · Entrez [101060146](https://www.ncbi.nlm.nih.gov/gene/101060146) · Ensembl [ENSG00000278530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278530)

## Data

Gene col 15914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15914); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15914]; `tensor/DDL_lfc|DDL_z.npy` [15914]; `embed/gene_vectors.npy` [15914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15914 or target_col == 15914). Every well: [[CHMP1B2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP1B2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
