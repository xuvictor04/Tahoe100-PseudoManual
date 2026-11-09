---
symbol: "CXCL10"
type: "gene"
col: 9783
ensembl_id: "ENSG00000169245"
name: "C-X-C motif chemokine ligand 10"
location: "4q21.1"
module: 32
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 27
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# CXCL10

*C-X-C motif chemokine ligand 10* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.51× (z +11.7, q 1e-28, up in 10 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.144×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OASL]] (+0.78, fdr 7e-06), [[GBP1]] (+0.77, fdr 7e-06), [[IFIH1]] (+0.75, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 9 go from it, the strongest it → [[IFIT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.51×** | +11.7 | 1e-28 | 10/17 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **6.37×** | +8.2 | 7e-14 | 9/17 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.12×** | +7.9 | 5e-13 | 9/16 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.93×** | +7.9 | 5e-13 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.44×** | +7.2 | 7e-11 | 13/23 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +6.9 | 5e-10 | 4/15 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.89×** | +6.6 | 5e-09 | 1/8 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.17×** | +6.4 | 1e-08 | 1/6 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **3.97×** | +6.1 | 7e-08 | 9/16 (A498, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.52×** | +4.5 | 5e-04 | 3/16 (LS 180, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **2.12×** | +4.4 | 5e-04 | 5/19 (CFPAC-1, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.34×** | +3.8 | 0.008 | 4/16 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Vortioxetine (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.6 | 0.014 | 4/16 (BT-474, A-172, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.91×** | +3.5 | 0.016 | 6/21 (CFPAC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **2.05×** | +3.5 | 0.021 | 6/21 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **2.09×** | +3.3 | 0.025 | 3/15 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +3.3 | 0.025 | 3/16 (NCI-H460, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[venetoclax (drug)]] 0.05 µM |  | **2.01×** | +3.2 | 0.042 | 2/16 (LS 180, Panc 03.27) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.82×** | +3.1 | 0.055 | 5/22 (CFPAC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9783.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.144×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | 0.466× | -3.5 | 0.25 | 10/15 (A498, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.634× | -3.1 | 0.47 | 9/17 (A498, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 24.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +12.2) | [[Selinexor (drug)]] 5 µM 0.144× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.156 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.278 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.592 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.619 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.778 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.883 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.209 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.722 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.691 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.173 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OASL]] | +0.78 | +0.67 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 717 |
| [[GBP1]] | +0.77 | +0.67 / +0.78 | both halves | 7e-06 | STRING 887 |
| [[IFIH1]] | +0.75 | +0.66 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 891 |
| [[IFIT2]] | +0.75 | +0.67 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 852 |
| [[EPSTI1]] | +0.74 | +0.63 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 535 |
| [[GBP4]] | +0.73 | +0.62 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 776 |
| [[RIGI]] | +0.73 | +0.63 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 854 |
| [[CCL5]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 999 |
| [[GBP5]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 | STRING 749 |
| [[IFIT3]] | +0.71 | +0.61 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 829 |
| [[DDX60]] | +0.71 | +0.61 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 534 |
| [[DHX58]] | +0.70 | +0.59 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 631 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CXCL10's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[TNIP3]] | C | TNIP3 activity raises CXCL10's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 2.35× lower at baseline in the lines without TNIP3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA; co-absent with the target |
| [[CCL5]] | C | CCL5 activity raises CXCL10's level | lines that do not express CCL5 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without CCL5 | 0.059 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIT2]] | B | CXCL10 activity raises IFIT2's level | lines that do not express CXCL10 (23) vs lines expressing it (27) | 2.61× lower at baseline in the lines without CXCL10 | 0.017 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent |
| [[RIGI]] | B | CXCL10 activity weakens RIGI's drug response | lines that do not express CXCL10 (20) vs lines expressing it (26) | the lines without CXCL10 respond 1.35× as strongly (z diff -1.21); strongest at Tofacitinib 0.5 µM: 0.35x vs 0.54x (z diff -2.7) | 0.020 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent; target measured in part of the lines |
| [[B2M]] | B | CXCL10 activity raises B2M's level | lines that do not express CXCL10 (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without CXCL10 | 0.025 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent |
| [[OASL]] | B | CXCL10 activity raises OASL's level | lines that do not express CXCL10 (23) vs lines expressing it (27) | 2.49× lower at baseline in the lines without CXCL10 | 0.056 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent |
| [[TEX41]] | B | CXCL10 activity raises TEX41's level | lines that do not express CXCL10 (23) vs lines expressing it (27) | 3.33× lower at baseline in the lines without CXCL10 | 0.070 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent |
| [[IFIT1]] | B | CXCL10 activity weakens IFIT1's drug response | lines that do not express CXCL10 (19) vs lines expressing it (26) | the lines without CXCL10 respond 1.58× as strongly (z diff -1.87); strongest at Tofacitinib (citrate) 5 µM: 0.29x vs 0.59x (z diff -3.2) | 0.088 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent; target measured in part of the lines |
| [[ZC3HAV1]] | B | CXCL10 activity raises ZC3HAV1's level | lines that do not express CXCL10 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without CXCL10 | 0.094 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent |
| [[CCL5]] | C | CXCL10 activity raises CCL5's level | lines that do not express CXCL10 (23) vs lines expressing it (27) | 3.73× lower at baseline in the lines without CXCL10 | 0.022 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent; co-absent with the target |
| [[IL6]] | C | CXCL10 activity raises IL6's level | lines that do not express CXCL10 (23) vs lines expressing it (27) | 3.82× lower at baseline in the lines without CXCL10 | 0.081 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.9, 52.1); signed map (62.8, 30.4). **Vector** length 42.5, 10.2% of its response variance represented; |z| ≥ 3 in 377 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.66 to 23); *Interferon Signaling* (reactome, mean cos +0.60 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.62 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.4 | +8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.9 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +4.4 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.4 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.3 | -3.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | C-X-C motif chemokine ligand 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:76,021,118-76,023,497 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IFI10, IP-10, crg-2, mob-1, C7, gIP-10; previously INP10, SCYB10 |
| Gene groups (HGNC) | Chemokine ligands |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INTERFERON_ALPHA_RESPONSE, INFLAMMATORY_RESPONSE, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 10 pathways, smallest: Chemokine receptors bind chemokines; Interleukin-10 signaling; Peptide ligand-binding receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P02778](https://www.uniprot.org/uniprotkb/P02778) (C-X-C motif chemokine 10):

> Pro-inflammatory cytokine that is involved in a wide variety of processes such as chemotaxis, differentiation, and activation of peripheral immune cells, regulation of cell growth, apoptosis and modulation of angiostatic effects. Plays thereby an important role during viral infections by stimulating the activation and migration of immune cells to the infected sites (By similarity). Mechanistically, binding of CXCL10 to the CXCR3 receptor activates G protein-mediated signaling and results in …

**Summary**, from NCBI Gene [3627](https://www.ncbi.nlm.nih.gov/gene/3627):

> This antimicrobial gene encodes a chemokine of the CXC subfamily and ligand for the receptor CXCR3. Binding of this protein to CXCR3 results in pleiotropic effects, including stimulation of monocytes, natural killer and T-cell migration, and modulation of adhesion molecule expression. This gene may also be a key regulator of the 'cytokine storm' immune response to SARS-CoV-2 infection. [provided by RefSeq, Sep 2020]

**Accessions** — [HGNC:10637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10637) · Entrez [3627](https://www.ncbi.nlm.nih.gov/gene/3627) · UniProt [P02778](https://www.uniprot.org/uniprotkb/P02778) · Ensembl [ENSG00000169245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169245)

## Data

Gene col 9783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9783); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9783]; `tensor/DDL_lfc|DDL_z.npy` [9783]; `embed/gene_vectors.npy` [9783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9783 or target_col == 9783). Every well: [[CXCL10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXCL10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
