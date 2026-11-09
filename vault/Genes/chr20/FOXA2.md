---
symbol: "FOXA2"
type: "gene"
col: 4663
ensembl_id: "ENSG00000125798"
name: "forkhead box A2"
location: "20p11.21"
module: 20
arm: "-"
pooled_cpm: 15.06
n_lines_expressing: 22
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# FOXA2

*forkhead box A2* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.78× (z +6.0, q 1e-06, up in 12 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.527× (z -4.7, q 0.002, down in 16 of 19 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF503]] (+0.77, fdr 7e-06), [[IRX5]] (+0.70, fdr 7e-06), [[EID2]] (+0.67, fdr 1e-05); moves opposite to [[VAMP3]] (-0.69, fdr 1e-05), [[PABIR2]] (-0.66, fdr 1e-05), [[FAM91A1]] (-0.66, fdr 2e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 4 go from it, the strongest it → [[ATXN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4663.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +6.0 | 1e-06 | 12/20 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.73×** | +5.7 | 3e-06 | 10/19 (A549, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.97×** | +5.0 | 1e-04 | 12/19 (Hs 766T, SW480, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +4.4 | 0.002 | 12/19 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +4.2 | 0.003 | 0/15 | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.80×** | +4.2 | 0.003 | 14/19 (A549, COLO 205, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.9 | 0.007 | 7/19 (KATO III, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **1.70×** | +3.9 | 0.007 | 9/19 (PANC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.63×** | +3.6 | 0.021 | 12/19 (A549, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.60×** | +3.4 | 0.032 | 13/19 (A549, A498, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.066 | 9/19 (LoVo, SW480, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.074 | 9/19 (A498, COLO 205, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.51×** | +3.0 | 0.100 | 0/18 | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4663.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.527×** | -4.7 | 0.002 | 16/19 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.576×** | -3.7 | 0.045 | 6/19 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.605×** | -3.7 | 0.045 | 14/19 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.632× | -3.4 | 0.10 | 8/19 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.612× | -3.3 | 0.10 | 3/19 (A549, SHP-77, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.652× | -3.1 | 0.17 | 10/19 (SHP-77, LoVo, …) | top dose only |  |
| [[Encorafenib (drug)]] 5 µM |  | 0.454× | -3.0 | 0.17 | 1/20 (Hs 766T) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.662× | -3.0 | 0.17 | 12/19 (NCI-H1792, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.80 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 34.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 5.54× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 53.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -12.1) |
| [[SW 900 (line)]] | alt | 45.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -11.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 40.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -11.5) |
| [[A498 (line)]] | wt | 16.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -9.4) |
| [[Hs 766T (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -10.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0603× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[KATO III (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -10.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[LS 180 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H1573 (line)]] | alt | 29.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF503]] | +0.77 | +0.59 / +0.81 | both halves | 7e-06 |  |
| [[IRX5]] | +0.70 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[EID2]] | +0.67 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[FOXD1]] | +0.66 | +0.55 / +0.63 | both halves | 1e-05 | same gene group; STRING 480 |
| [[METTL23]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[POLR1H]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.65 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[SCAND1]] | +0.65 | +0.41 / +0.71 | both halves | 4e-05 |  |
| [[ZBTB7A]] | +0.63 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[PURA]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[MED19]] | +0.62 | +0.38 / +0.72 | both halves | 7e-05 |  |
| [[REST]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAMP3]] | -0.69 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[PABIR2]] | -0.66 | -0.49 / -0.72 | both halves | 1e-05 |  |
| [[FAM91A1]] | -0.66 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[DHFR]] | -0.65 | -0.43 / -0.72 | both halves | 3e-05 |  |
| [[MAN2B2]] | -0.65 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[VTI1B]] | -0.64 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[RPSA]] | -0.64 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[OPA1]] | -0.63 | -0.47 / -0.72 | both halves | 2e-05 |  |
| [[ZNF731P]] | -0.62 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[UBQLN1]] | -0.62 | -0.46 / -0.73 | both halves | 3e-05 |  |
| [[AGO1]] | -0.61 | -0.38 / -0.68 | both halves | 6e-05 | pathway: Adherens junctions interactions |
| [[DROSHA]] | -0.60 | -0.59 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FOXA2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SOX2]] | C | SOX2 activity raises FOXA2's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without SOX2 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN2]] | B | FOXA2 activity lowers ATXN2's level | lines that do not express FOXA2 (28) vs lines expressing it (22) | 1.28× higher at baseline in the lines without FOXA2 | 0.015 | ⚠ within organs, on part of the lines; also absent: TFF1, GPX2, F5 |
| [[ZNF703]] | B | FOXA2 activity raises ZNF703's level | lines that do not express FOXA2 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without FOXA2 | 0.018 | ⚠ within organs, on part of the lines; also absent: TFF1, GPX2, F5 |
| [[AHSA1]] | B | FOXA2 activity lowers AHSA1's level | lines that do not express FOXA2 (28) vs lines expressing it (22) | 1.26× higher at baseline in the lines without FOXA2 | 0.078 | ⚠ within organs, on part of the lines; also absent: TFF1, GPX2, F5 |
| [[MT1G]] | C | FOXA2 activity raises MT1G's level | lines that do not express FOXA2 (28) vs lines expressing it (22) | 2.52× lower at baseline in the lines without FOXA2 | 0.076 | ⚠ within organs, on part of the lines; also absent: TFF1, GPX2, F5; co-absent with the target |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.8, -23.9); signed map (-3.7, 8.7). **Vector** length 59.7, 19.7% of its response variance represented; |z| ≥ 3 in 321 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +4.0 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.3 | +3.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | -1.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -3.7 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -3.4 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -3.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:22,580,998-22,585,455 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HNF3B |
| Gene groups (HGNC) | Forkhead boxes |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Reactome | 14 pathways, smallest: Regulation of gene expression in beta cells; Formation of definitive endoderm; Formation of axial mesoderm |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y261](https://www.uniprot.org/uniprotkb/Q9Y261) (Hepatocyte nuclear factor 3-beta):

> Transcription factor that is involved in embryonic development, establishment of tissue-specific gene expression and regulation of gene expression in differentiated tissues. Is thought to act as a 'pioneer' factor opening the compacted chromatin for other proteins through interactions with nucleosomal core histones and thereby replacing linker histones at target enhancer and/or promoter sites. Binds DNA with the consensus sequence 5'-[AC]A[AT]T[AG]TT[GT][AG][CT]T[CT]-3' (By similarity). In …

**Summary**, from NCBI Gene [3170](https://www.ncbi.nlm.nih.gov/gene/3170):

> This gene encodes a member of the forkhead class of DNA-binding proteins. These hepatocyte nuclear factors are transcriptional activators for liver-specific genes such as albumin and transthyretin, and they also interact with chromatin. Similar family members in mice have roles in the regulation of metabolism and in the differentiation of the pancreas and liver. This gene has been linked to sporadic cases of maturity-onset diabetes of the young. Transcript variants encoding different isoforms …

**Accessions** — [HGNC:5022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5022) · Entrez [3170](https://www.ncbi.nlm.nih.gov/gene/3170) · UniProt [Q9Y261](https://www.uniprot.org/uniprotkb/Q9Y261) · Ensembl [ENSG00000125798](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125798)

## Data

Gene col 4663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4663); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4663]; `tensor/DDL_lfc|DDL_z.npy` [4663]; `embed/gene_vectors.npy` [4663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4663 or target_col == 4663). Every well: [[FOXA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
