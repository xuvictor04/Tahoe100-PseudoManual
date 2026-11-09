---
symbol: "H2AZ1-DT"
type: "gene"
col: 14428
ensembl_id: "ENSG00000245322"
name: "H2AZ1 divergent transcript"
location: "4q23"
module: 26
arm: "+"
pooled_cpm: 2.55
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# H2AZ1-DT

*H2AZ1 divergent transcript* — 4q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 16.6× (z +32.2, q 0e+00, up in 30 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (NCI-H460 0.0878×); [[Pimozide (drug)]] 0.5 µM in 1 line (HOP62 0.0889×; ⚠ transcription drop).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS6-AS1]] (+0.88, fdr 7e-06), [[NEB]] (+0.83, fdr 7e-06), [[CASS4]] (+0.82, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DRAIC]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **16.6×** | +32.2 | 0e+00 | 30/30 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **6.24×** | +21.0 | 0e+00 | 36/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **6.34×** | +14.4 | 1e-44 | 24/26 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **5.57×** | +13.4 | 9e-39 | 29/34 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.08×** | +11.4 | 5e-28 | 28/32 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.24×** | +9.5 | 1e-19 | 35/45 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.09×** | +8.5 | 2e-15 | 20/43 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.65×** | +7.9 | 2e-13 | 23/40 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **2.51×** | +7.5 | 5e-12 | 27/43 (A498, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.48×** | +7.4 | 9e-12 | 27/41 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.39×** | +7.1 | 8e-11 | 24/43 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.28×** | +6.4 | 6e-09 | 18/39 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +5.4 | 2e-06 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +5.1 | 2e-05 | 2/10 (HEC-1-A, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.85×** | +5.0 | 2e-05 | 14/44 (A-172, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.002 | 11/44 (A-172, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +3.7 | 0.006 | 8/44 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (NCI-H460 0.0878×); [[Pimozide (drug)]] 0.5 µM in 1 line (HOP62 0.0889×; ⚠ transcription drop).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.65 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 30.5× (z +17.1) | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0878× (z -8.6) |
| [[HOP62 (line)]] | alt | 4.04 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.8× (z +14.3) | [[Pimozide (drug)]] 0.5 µM 0.0889× (z -8.6) ⚠ transcription drop |
| [[A498 (line)]] | wt | 2.96 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +12.5) | — |
| [[C32 (line)]] | wt | 3.43 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 4.94 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +12.7) | — |
| [[J82 (line)]] | alt | 2.71 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +10.5) | — |
| [[LoVo (line)]] | wt | 2.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.6× (z +15.1) | — |
| [[LS 180 (line)]] | wt | 3.34 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 3.48 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 2.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +10.1) | — |
| [[A-172 (line)]] | wt | 2.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.6× (z +11.2) | — |
| [[A549 (line)]] | wt | 1.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.3× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.5× (z +11.1) | — |
| [[HCT15 (line)]] | alt | 2.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.6× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.8× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 1.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 41.5× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 4.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +8.5) | — |
| [[KATO III (line)]] | alt | 2.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.8× (z +13.1) | — |
| [[NCI-H23 (line)]] | alt | 5.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.07× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 1.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.0× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 1.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 44.6× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 2.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +14.1) | — |
| [[RPMI-7951 (line)]] | alt | 2.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 1.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 2.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.9× (z +10.5) | — |
| [[SW480 (line)]] | alt | 1.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +11.0) | — |
| [[A-427 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6-AS1]] | +0.88 | +0.88 / +0.79 | both halves | 7e-06 |  |
| [[NEB]] | +0.83 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[CASS4]] | +0.82 | +0.86 / +0.59 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.82 | +0.85 / +0.59 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.81 | +0.78 / +0.60 | both halves | 7e-06 | same gene group |
| [[PSMD14-DT]] | +0.80 | +0.84 / +0.61 | both halves | 7e-06 | same gene group |
| [[PPP1R12A-AS2]] | +0.80 | +0.86 / +0.50 | both halves | 1e-05 |  |
| [[SEPTIN7-DT]] | +0.80 | +0.81 / +0.62 | both halves | 7e-06 | same gene group |
| [[USP38-DT]] | +0.79 | +0.79 / +0.71 | both halves | 7e-06 | same gene group |
| [[DNAH12]] | +0.79 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[UNC79]] | +0.79 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[CIBAR1-DT]] | +0.78 | +0.81 / +0.55 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers H2AZ1-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[DDR2]] | B | DDR2 activity raises H2AZ1-DT's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without DDR2 | 0.047 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[LINC01917]] | B | LINC01917 activity raises H2AZ1-DT's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without LINC01917 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[ANKRD7]] | B | ANKRD7 activity raises H2AZ1-DT's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without ANKRD7 | 0.066 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[COP1-DT]] | B | COP1-DT activity raises H2AZ1-DT's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without COP1-DT | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[FBXO38-DT]] | C | FBXO38-DT activity raises H2AZ1-DT's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.34× lower at baseline in the lines without FBXO38-DT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DRAIC]] | C | H2AZ1-DT's natural level strengthens DRAIC's drug response | H2AZ1-DT's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.05; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.820). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.8, 17.6); signed map (24.3, -0.4). **Vector** length 60.0, 8.71% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +32.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +21.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +2.6 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +0.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.6 | +7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | +1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | +0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | H2AZ1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q23 — chr4:99,950,006-100,195,099 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40271) · Entrez [256880](https://www.ncbi.nlm.nih.gov/gene/256880) · Ensembl [ENSG00000245322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245322)

## Data

Gene col 14428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14428); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14428]; `tensor/DDL_lfc|DDL_z.npy` [14428]; `embed/gene_vectors.npy` [14428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14428 or target_col == 14428). Every well: [[H2AZ1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H2AZ1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
