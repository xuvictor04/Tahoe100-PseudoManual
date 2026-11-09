---
symbol: "FAM110B"
type: "gene"
col: 9756
ensembl_id: "ENSG00000169122"
name: "family with sequence similarity 110 member B"
location: "8q12.1"
module: 9
arm: "+"
pooled_cpm: 12.16
n_lines_expressing: 23
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 31
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# FAM110B

*family with sequence similarity 110 member B* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.91× (z +13.5, q 5e-39, up in 18 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2030 0.159×, J82 0.168×, C32 0.0777×, NCI-H1792 0.128×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2030 0.0233×, J82 0.243×, C32 0.132×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CHP-212 0.117×, NCI-H2030 0.442×, HepG2/C3A 0.256×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0797×); [[Allantoin (drug)]] 0.5 µM in 1 line (H4 0.0589×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FSTL5]] (+0.65, fdr 1e-05), [[DISC1FP1]] (+0.62, fdr 2e-05), [[NGF]] (+0.62, fdr 1e-05); moves opposite to [[ODF2]] (-0.44, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KLHL13]] → it (grade C ⚠); 3 go from it, the strongest it → [[LINC03046]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +13.5 | 5e-39 | 18/21 (NCI-H460, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +13.2 | 2e-37 | 13/21 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +9.5 | 3e-19 | 6/20 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +8.6 | 1e-15 | 13/21 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +8.5 | 2e-15 | 1/20 (H4) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +8.1 | 6e-14 | 11/21 (BT-474, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +7.6 | 2e-12 | 14/21 (A498, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +6.9 | 4e-10 | 12/21 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +6.6 | 2e-09 | 13/21 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +6.5 | 4e-09 | 9/21 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +6.0 | 1e-07 | 7/21 (BT-474, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +5.8 | 4e-07 | 17/21 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.7 | 4e-07 | 8/21 (C32, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +5.5 | 2e-06 | 12/21 (A498, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.4 | 3e-06 | 2/21 (NCI-H460, A498) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 5e-06 | 11/21 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 1e-04 | 10/21 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +4.6 | 2e-04 | 12/21 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9756.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2030 0.159×, J82 0.168×, C32 0.0777×, NCI-H1792 0.128×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2030 0.0233×, J82 0.243×, C32 0.132×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CHP-212 0.117×, NCI-H2030 0.442×, HepG2/C3A 0.256×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0797×); [[Allantoin (drug)]] 0.5 µM in 1 line (H4 0.0589×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.785× | -3.6 | 0.16 | 1/21 (BT-474) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.866× | -3.1 | 0.40 | 2/21 (CFPAC-1, SNU-423) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | 0.815× | -3.1 | 0.40 | 3/21 (CFPAC-1, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 65.1 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +14.1) | — |
| [[NCI-H2030 (line)]] | alt | 85.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0233× (z -32.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -10.3) |
| [[A498 (line)]] | wt | 12.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +15.4) | — |
| [[C32 (line)]] | wt | 21.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0777× (z -12.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 58.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -14.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 77.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -13.8) |
| [[H4 (line)]] | wt | 17.2 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0589× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 24.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -9.4) |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 4.71 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0797× (z -11.3) |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.968 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.934 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.940 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSTL5]] | +0.65 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[DISC1FP1]] | +0.62 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[NGF]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[LINC01320]] | +0.58 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[FMN2]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[RGS7]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[LINC02241]] | +0.57 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[MIR155HG]] | +0.56 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[MARCHF1]] | +0.56 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ANKRD30B]] | +0.56 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[LINC01695]] | +0.56 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[ROR1-AS1]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ODF2]] | -0.44 | -0.36 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL13]] | C | KLHL13 activity raises FAM110B's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without KLHL13 | 0.039 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |
| [[CNKSR2]] | C | CNKSR2 activity raises FAM110B's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 4.41× lower at baseline in the lines without CNKSR2 | 0.095 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03046]] | C | FAM110B activity raises LINC03046's level | lines that do not express FAM110B (27) vs lines expressing it (23) | 2.35× lower at baseline in the lines without FAM110B | 0.042 | ⚠ within organs, on part of the lines; also absent: LRRK2, PIEZO2, GFRA1; co-absent with the target |
| [[KLHL13]] | C | FAM110B activity raises KLHL13's level | lines that do not express FAM110B (27) vs lines expressing it (23) | 2.16× lower at baseline in the lines without FAM110B | 0.044 | ⚠ within organs, on part of the lines; also absent: LRRK2, PIEZO2, GFRA1; co-absent with the target |
| [[PTPRM]] | C | FAM110B activity raises PTPRM's level | lines that do not express FAM110B (27) vs lines expressing it (23) | 4.41× lower at baseline in the lines without FAM110B | 0.095 | ⚠ within organs, on part of the lines; also absent: LRRK2, PIEZO2, GFRA1; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.4, 27.5); signed map (38.5, 26.4). **Vector** length 50.5, 11.2% of its response variance represented; |z| ≥ 3 in 521 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.7 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | -0.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | +0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | +0.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -0.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 110 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:57,994,523-58,204,279 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39325; previously C8orf72 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC76](https://www.uniprot.org/uniprotkb/Q8TC76) (Protein FAM110B):

> May be involved in tumor progression.

**Summary**, from NCBI Gene [90362](https://www.ncbi.nlm.nih.gov/gene/90362):

> Located in cytosol and mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28587) · Entrez [90362](https://www.ncbi.nlm.nih.gov/gene/90362) · UniProt [Q8TC76](https://www.uniprot.org/uniprotkb/Q8TC76) · Ensembl [ENSG00000169122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169122)

## Data

Gene col 9756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9756); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9756]; `tensor/DDL_lfc|DDL_z.npy` [9756]; `embed/gene_vectors.npy` [9756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9756 or target_col == 9756). Every well: [[FAM110B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM110B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
