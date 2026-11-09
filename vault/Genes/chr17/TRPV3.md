---
symbol: "TRPV3"
type: "gene"
col: 9529
ensembl_id: "ENSG00000167723"
name: "transient receptor potential cation channel subfamily V member 3"
location: "17p13.2"
module: 101
arm: "+"
pooled_cpm: 3.14
n_lines_expressing: 38
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# TRPV3

*transient receptor potential cation channel subfamily V member 3* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.89× (z +22.2, q 0e+00, up in 22 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Budesonide (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0492×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.0510×; ⚠ cell-cycle shift, explains ~0% of this change); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (NCI-H1573 0.0813×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (A-172 0.0797×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX9]] (+0.62, fdr 1e-05), [[C6orf141]] (+0.62, fdr 1e-05), [[IL23A]] (+0.61, fdr 1e-05); moves opposite to [[TMEM245]] (-0.49, fdr 4e-05), [[LGR4]] (-0.47, fdr 9e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[OVOL1]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Homoharringtonine (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.89×** | +22.2 | 0e+00 | 22/25 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.39×** | +21.1 | 0e+00 | 16/25 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.61×** | +11.3 | 2e-27 | 4/12 (HOP62, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.95×** | +11.0 | 9e-26 | 1/5 (AsPC-1) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.25×** | +10.4 | 3e-23 | 18/25 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +7.7 | 1e-12 | 0/2 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.39×** | +7.7 | 1e-12 | 16/30 (HepG2/C3A, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.07×** | +6.4 | 9e-09 | 12/30 (HepG2/C3A, COLO 205, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +6.0 | 1e-07 | 6/17 (HepG2/C3A, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.97×** | +5.7 | 6e-07 | 14/29 (COLO 205, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.93×** | +5.5 | 2e-06 | 11/28 (HepG2/C3A, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +5.3 | 5e-06 | 10/29 (SW480, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +4.9 | 4e-05 | 12/32 (A-172, SW480, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.0 | 0.002 | 4/16 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.008 | 7/29 (SW48, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.042 | 9/31 (BT-474, HCT15, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.073 | 3/26 (NCI-H1573, A-172, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.077 | 3/30 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.088 | 1/29 (SW48) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9529.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Budesonide (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0492×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.0510×; ⚠ cell-cycle shift, explains ~0% of this change); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (NCI-H1573 0.0813×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (A-172 0.0797×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Megestrol (drug)]] 5 µM |  | 0.770× | -3.3 | 0.50 | 5/32 (NCI-H1573, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.28 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +13.2) | [[Cobimetinib (drug)]] 0.05 µM 0.0797× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 12.2 | 1 | 2 | [[Harringtonine (drug)]] 0.5 µM 11.4× (z +9.1) | [[Budesonide (drug)]] 0.5 µM 0.0492× (z -11.3) |
| [[COLO 205 (line)]] | alt | 5.95 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.4× (z +14.7) | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -8.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 4.40 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +10.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0510× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 0.961 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 1.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.58× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 1.10 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.0520× (z -8.5) |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 2.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +9.6) | — |
| [[A-427 (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.868 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.838 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX9]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[C6orf141]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[IL23A]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[KPNA7]] | +0.61 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[MYH16]] | +0.59 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[ARL14]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[LAMB3]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[HCG20]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[UPP1]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[RPLP0P2]] | +0.58 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[DNAH17]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[RNF223]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM245]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[LGR4]] | -0.47 | -0.42 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OVOL1]] | B | OVOL1 activity raises TRPV3's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.95× lower at baseline in the lines without OVOL1 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[RNF223]] | B | RNF223 activity raises TRPV3's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without RNF223 | 0.027 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[NOS3]] | B | NOS3 activity raises TRPV3's level | lines that do not express NOS3 (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without NOS3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ABO, GJB3, SYK |
| [[LINC01226]] | B | LINC01226 activity raises TRPV3's level | lines that do not express LINC01226 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without LINC01226 | 0.060 | ⚠ within organs, on part of the lines; also absent: LASTR, TRIM29, ENSG00000287003; maybe low, not absent |
| [[LAMC2]] | B | LAMC2 activity raises TRPV3's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.80× lower at baseline in the lines without LAMC2 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[MYO5B]] | B | MYO5B activity raises TRPV3's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 1.71× lower at baseline in the lines without MYO5B | 0.087 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Homoharringtonine (drug)]] 5 µM | B | TRPV3 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express TRPV3 (12) vs lines expressing it (36) | the lines without TRPV3: 0.41× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DNAH17]] | B | TRPV3 activity raises DNAH17's level | lines that do not express TRPV3 (12) vs lines expressing it (38) | 1.69× lower at baseline in the lines without TRPV3 | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.0, 0.1); signed map (2.6, 33.9). **Vector** length 62.1, 11.7% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +21.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +22.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +7.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -0.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily V member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,510,502-3,557,812 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VRL3 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Transient receptor potential cation channel subfamily V |
| Reactome | 4 pathways, smallest: TRP channels; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NET8](https://www.uniprot.org/uniprotkb/Q8NET8) (Transient receptor potential cation channel subfamily V member 3):

> Non-selective calcium permeant cation channel. It is activated by innocuous (warm) temperatures and shows an increased response at noxious temperatures greater than 39 degrees Celsius. Activation exhibits an outward rectification. The channel pore can dilate to provide permeability to larger cations. May associate with TRPV1 and may modulate its activity. Is a negative regulator of hair growth and cycling: TRPV3-coupled signaling suppresses keratinocyte proliferation in hair follicles and …

**Summary**, from NCBI Gene [162514](https://www.ncbi.nlm.nih.gov/gene/162514):

> This gene product belongs to a family of nonselective cation channels that function in a variety of processes, including temperature sensation and vasoregulation. The thermosensitive members of this family are expressed in subsets of sensory neurons that terminate in the skin, and are activated at distinct physiological temperatures. This channel is activated at temperatures between 22 and 40 degrees C. This gene lies in close proximity to another family member gene on chromosome 17, and the …

**Accessions** — [HGNC:18084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18084) · Entrez [162514](https://www.ncbi.nlm.nih.gov/gene/162514) · UniProt [Q8NET8](https://www.uniprot.org/uniprotkb/Q8NET8) · Ensembl [ENSG00000167723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167723)

## Data

Gene col 9529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9529); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9529]; `tensor/DDL_lfc|DDL_z.npy` [9529]; `embed/gene_vectors.npy` [9529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9529 or target_col == 9529). Every well: [[TRPV3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPV3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
