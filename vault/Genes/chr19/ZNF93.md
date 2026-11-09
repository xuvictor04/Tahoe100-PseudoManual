---
symbol: "ZNF93"
type: "gene"
col: 11561
ensembl_id: "ENSG00000184635"
name: "zinc finger protein 93"
location: "19p12"
module: 91
arm: "+"
pooled_cpm: 8.91
n_lines_expressing: 29
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 7
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# ZNF93

*zinc finger protein 93* — 19p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +7.7, q 8e-12, up in 14 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.702× (z -4.3, q 0.008, down in 13 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPL]] (+0.68, fdr 1e-05), [[ZNF100]] (+0.67, fdr 7e-06), [[ZNF714]] (+0.61, fdr 2e-05); moves opposite to [[PPP2R2A]] (-0.49, fdr 3e-05), [[CDA]] (-0.46, fdr 1e-04), [[STX7]] (-0.45, fdr 2e-04).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ZNF736]] → it (grade B ⚠); 7 go from it, the strongest it → [[ZNF736]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11561.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.7 | 8e-12 | 14/25 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.0 | 6e-07 | 9/24 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.0 | 1e-04 | 13/27 (PANC-1, COLO 205, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +5.0 | 1e-04 | 8/25 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.024 | 5/26 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.024 | 12/25 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | 1.21× | +3.2 | 0.10 | 3/27 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.20× | +3.1 | 0.16 | 5/27 (RPMI-7951, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11561.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.702×** | -4.3 | 0.008 | 13/26 (C32, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -3.9 | 0.030 | 12/27 (RPMI-7951, COLO 205, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.574×** | -3.6 | 0.071 | 13/26 (RPMI-7951, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.598× | -3.3 | 0.14 | 13/27 (AN3 CA, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 0.771× | -3.2 | 0.15 | 7/22 (A-172, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[palbociclib (drug)]] 0.5 µM |  | 0.709× | -3.0 | 0.24 | 0/27 | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11561. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 72.4 | 0 | 3 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0458× (z -16.7) |
| [[NCI-H2030 (line)]] | alt | 6.94 | 0 | 2 (2 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0744× (z -10.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 29.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 7.93 | 0 | 1 | — | [[Allantoin (drug)]] 5 µM 0.221× (z -9.2) |
| [[PANC-1 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.969 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11561), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPL]] | +0.68 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ZNF100]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 | same gene group |
| [[ZNF714]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 | same gene group |
| [[ZNF695]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 | same gene group |
| [[GEN1]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZNF724]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 | same gene group |
| [[HROB]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ZNF43]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 | same gene group |
| [[ORC6]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LRR1]] | +0.57 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[ZNF85]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 | same gene group; STRING 417 |
| [[DBF4B]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R2A]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CDA]] | -0.46 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[STX7]] | -0.45 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[SGSM1]] | -0.45 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[SLC2A3]] | -0.44 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[GPRC5A]] | -0.44 | -0.40 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF736]] | B | ZNF736 activity raises ZNF93's level | lines that do not express ZNF736 (19) vs lines expressing it (31) | 2.75× lower at baseline in the lines without ZNF736 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, IQCA1 |
| [[TOP2A]] | B | TOP2A activity lowers ZNF93's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF724]] | B | ZNF724 activity raises ZNF93's level | lines that do not express ZNF724 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without ZNF724 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577 |
| [[TOP2B]] | B | TOP2B activity lowers ZNF93's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ZNF850]] | B | ZNF850 activity raises ZNF93's level | lines that do not express ZNF850 (7) vs lines expressing it (43) | 3.09× lower at baseline in the lines without ZNF850 | 0.095 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF613, ZNF420 |
| [[ZNF486]] | C | ZNF486 activity raises ZNF93's level | lines that do not express ZNF486 (22) vs lines expressing it (28) | 3.26× lower at baseline in the lines without ZNF486 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, CDK15, ENSG00000287335; co-absent with the target |
| [[ZNF85]] | C | ZNF85 activity raises ZNF93's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 3.52× lower at baseline in the lines without ZNF85 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726; co-absent with the target |
| [[ZNF730]] | C | ZNF730 activity raises ZNF93's level | lines that do not express ZNF730 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without ZNF730 | 0.048 | ⚠ within organs, on part of the lines; also absent: ZNF667, LINC03047, ENSG00000288016; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF736]] | B | ZNF93 activity raises ZNF736's level | lines that do not express ZNF93 (21) vs lines expressing it (29) | 3.33× lower at baseline in the lines without ZNF93 | 0.021 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF682, ZNF347 |
| [[ZNF253]] | B | ZNF93 activity raises ZNF253's level | lines that do not express ZNF93 (21) vs lines expressing it (29) | 1.94× lower at baseline in the lines without ZNF93 | 0.029 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF682, ZNF347 |
| [[KIF23-AS1]] | B | ZNF93 activity lowers KIF23-AS1's level | lines that do not express ZNF93 (21) vs lines expressing it (29) | 1.49× higher at baseline in the lines without ZNF93 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF682, ZNF347 |
| [[NNT]] | B | ZNF93 activity raises NNT's level | lines that do not express ZNF93 (21) vs lines expressing it (29) | 1.88× lower at baseline in the lines without ZNF93 | 0.088 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF682, ZNF347 |
| [[ZNF506]] | C | ZNF93 activity raises ZNF506's level | lines that do not express ZNF93 (21) vs lines expressing it (29) | 3.17× lower at baseline in the lines without ZNF93 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF682, ZNF347; co-absent with the target |
| [[ZNF730]] | C | ZNF93 activity raises ZNF730's level | lines that do not express ZNF93 (21) vs lines expressing it (29) | 2.30× lower at baseline in the lines without ZNF93 | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF682, ZNF347; co-absent with the target |
| [[ZNF486]] | C | ZNF93 activity raises ZNF486's level | lines that do not express ZNF93 (21) vs lines expressing it (29) | 2.50× lower at baseline in the lines without ZNF93 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF682, ZNF347; co-absent with the target |

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-44.7, -47.5); signed map (-39.3, -35.6). **Vector** length 50.5, 10.1% of its response variance represented; |z| ≥ 3 in 508 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.51 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.53 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +1.7 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +2.6 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.1 | +2.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.0 | +0.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +0.9 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +0.8 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -1.9 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -1.4 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 93 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p12 — chr19:19,900,913-19,963,464 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HPF34, TF34, FLJ12488; previously ZNF505 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Reactome | 3 pathways, smallest: Regulation of endogenous retroelements by KRAB-ZFP proteins; Regulation of endogenous retroelements; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P35789](https://www.uniprot.org/uniprotkb/P35789) (Zinc finger protein 93):

> Transcription factor specifically required to repress long interspersed nuclear element 1 (L1) retrotransposons: recognizes and binds L1 sequences and repress their expression by recruiting a repressive complex containing TRIM28/KAP1. Not able to repress expression of all subtypes of L1 elements. Binds to the 5' end of L1PA4, L1PA5 and L1PA6 subtypes, and some L1PA3 subtypes. Does not bind to L1PA7 or older subtypes nor at the most recently evolved L1PA2 and L1Hs. 50% of L1PA3 elements have …

**Summary**, from NCBI Gene [81931](https://www.ncbi.nlm.nih.gov/gene/81931):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific. Involved in transposable element silencing. Predicted to be located in nucleoplasm. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13169) · Entrez [81931](https://www.ncbi.nlm.nih.gov/gene/81931) · UniProt [P35789](https://www.uniprot.org/uniprotkb/P35789) · Ensembl [ENSG00000184635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184635)

## Data

Gene col 11561: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11561); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11561, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11561]; `tensor/DDL_lfc|DDL_z.npy` [11561]; `embed/gene_vectors.npy` [11561]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11561 or target_col == 11561). Every well: [[ZNF93 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF93.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
