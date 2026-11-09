---
symbol: "SPAG17"
type: "gene"
col: 7917
ensembl_id: "ENSG00000155761"
name: "sperm associated antigen 17"
location: "1p12"
module: 150
arm: "+"
pooled_cpm: 5.65
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# SPAG17

*sperm associated antigen 17* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.39× (z +19.5, q 0e+00, up in 18 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.0702×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.134×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGBL4]] (+0.71, fdr 7e-06), [[SYNPO2]] (+0.68, fdr 1e-05), [[LINC01725]] (+0.67, fdr 1e-05).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC01205]] → it (grade B ⚠); 1 goes from it, the strongest it → [[XKR9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.39×** | +19.5 | 0e+00 | 18/26 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +15.5 | 0e+00 | 17/29 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +10.1 | 1e-21 | 2/6 (A-427, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +9.1 | 2e-17 | 3/12 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +8.9 | 7e-17 | 3/13 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.06×** | +8.2 | 3e-14 | 14/35 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.8 | 4e-07 | 4/38 (NCI-H2347, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.6 | 2e-06 | 6/32 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.1 | 2e-05 | 10/28 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +5.0 | 3e-05 | 7/32 (C32, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.0 | 3e-05 | 3/23 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.001 | 9/37 (NCI-H23, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +4.0 | 0.002 | 0/11 | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.007 | 7/33 (NCI-H2347, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.7 | 0.009 | 1/18 (NCI-H2347) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.013 | 6/38 (NCI-H460, C32, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.025 | 7/32 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.061 | 2/23 (LOX-IMVI, SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.086 | 3/32 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +2.9 | 0.099 | 6/28 (SK-MEL-2, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7917.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.0702×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.134×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.794× | -3.7 | 0.12 | 10/37 (CFPAC-1, hTERT-HPNE, …) | top dose only |  |
| [[Fumaric acid (drug)]] 5 µM |  | 0.728× | -3.5 | 0.14 | 6/38 (C-33 A, hTERT-HPNE, …) | top dose only | plate-row cell shift; position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.811× | -3.4 | 0.14 | 7/37 (Panc 03.27, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 4.39 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 3.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 3.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 7.47 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0702× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -9.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 4.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +10.0) | — |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGBL4]] | +0.71 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[SYNPO2]] | +0.68 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[LINC01725]] | +0.67 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[STPG2]] | +0.64 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[LRRN3]] | +0.64 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[LINC01414]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD31]] | +0.63 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[LRRC4C]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[KCNT2]] | +0.63 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[LINC00240]] | +0.62 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[MYO16]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[AGA-DT]] | +0.62 | +0.72 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01205]] | B | LINC01205 activity raises SPAG17's level | lines that do not express LINC01205 (44) vs lines expressing it (6) | 3.52× lower at baseline in the lines without LINC01205 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, ENSG00000241168, GPR15; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SPAG17's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANKRD20A8P]], [[FAM95A]] | B | ANKRD20A8P, FAM95A activity raises SPAG17's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 2.40× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent genes |
| [[LINC00648]] | B | LINC00648 activity raises SPAG17's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 2.08× lower at baseline in the lines without LINC00648 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XKR9]] | B | SPAG17 activity lowers XKR9's level | lines that do not express SPAG17 (6) vs lines expressing it (44) | 2.23× higher at baseline in the lines without SPAG17 | 0.074 | ⚠ within organs, on part of the lines; also absent: NKAIN1, CEP85L, EMP3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.4, 25.4); signed map (38.0, 15.9). **Vector** length 47.7, 6.71% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +15.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +19.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +0.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.4 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | sperm associated antigen 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p12 — chr1:117,953,590-118,185,228 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34497, PF6, RP4-776P7.2, CT143 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6Q759](https://www.uniprot.org/uniprotkb/Q6Q759) (Sperm-associated antigen 17):

> Component of the central pair apparatus of ciliary axonemes. Plays a critical role in the function and structure of motile cilia. May play a role in endochondral bone formation, most likely because of a function in primary cilia of chondrocytes and osteoblasts (By similarity). Essential for normal spermatogenesis and male fertility (By similarity). Required for normal manchette structure, transport of proteins along the manchette microtubules and formation of the sperm head and flagellum (By …

**Summary**, from NCBI Gene [200162](https://www.ncbi.nlm.nih.gov/gene/200162):

> This gene encodes a central pair protein present in the axonemes of cells with a "9 + 2" organization of microtubules. The encoded protein is required for the proper function of the axoneme. Mutations in the orthologous gene in mice lead to primary ciliary dyskinesia characterized by immotile nasal and tracheal cilia, reduced clearance of nasal mucus, profound respiratory distress, hydrocephalus, and neonatal lethality within twelve hours of birth due to impaired airway mucociliary clearance. …

**Accessions** — [HGNC:26620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26620) · Entrez [200162](https://www.ncbi.nlm.nih.gov/gene/200162) · UniProt [Q6Q759](https://www.uniprot.org/uniprotkb/Q6Q759) · Ensembl [ENSG00000155761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155761)

## Data

Gene col 7917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7917); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7917]; `tensor/DDL_lfc|DDL_z.npy` [7917]; `embed/gene_vectors.npy` [7917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7917 or target_col == 7917). Every well: [[SPAG17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPAG17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
