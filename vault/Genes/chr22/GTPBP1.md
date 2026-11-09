---
symbol: "GTPBP1"
type: "gene"
col: 1897
ensembl_id: "ENSG00000100226"
name: "GTP binding protein 1"
location: "22q13.1"
module: 32
arm: "+"
pooled_cpm: 48.84
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# GTPBP1

*GTP binding protein 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 2.74× (z +6.9, q 3e-09, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.653× (z -7.9, q 2e-12, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAPA]] (+0.64, fdr 2e-05), [[SLC25A28]] (+0.59, fdr 1e-05), [[PML]] (+0.58, fdr 1e-05); moves opposite to [[MRPS9]] (-0.58, fdr 1e-05), [[THUMPD2]] (-0.56, fdr 1e-05), [[ACBD6]] (-0.56, fdr 3e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1897.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.74×** | +6.9 | 3e-09 | 40/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.4 | 6e-08 | 35/49 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +5.9 | 5e-07 | 42/49 (HT-29, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +5.7 | 2e-06 | 34/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.007 | 24/48 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.025 | 24/49 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.025 | 27/48 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +3.5 | 0.039 | 22/48 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1897.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.653×** | -7.9 | 2e-12 | 38/48 (SK-MEL-2, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.710×** | -4.5 | 0.002 | 29/48 (SNU-423, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -4.1 | 0.007 | 25/41 (A549, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.560×** | -4.0 | 0.010 | 28/48 (AsPC-1, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.744×** | -3.9 | 0.012 | 26/48 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.578×** | -3.8 | 0.016 | 26/48 (Hs 766T, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.759×** | -3.6 | 0.024 | 28/48 (SNU-423, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.617×** | -3.3 | 0.067 | 24/48 (AsPC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.7 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.8) | — |
| [[A549 (line)]] | wt | 55.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0605× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.416× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 50.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 37.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.461× (z -9.6) |
| [[A-427 (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 80.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -8.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 66.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.355× (z -10.0) |
| [[LoVo (line)]] | wt | 80.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 82.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 41.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 55.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H661 (line)]] | alt | 42.6 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0924× (z -8.5) |
| [[PANC-1 (line)]] | alt | 31.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 76.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.477× (z -10.3) |
| [[SNU-1 (line)]] | wt | 45.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.153× (z -11.3) |
| [[SW48 (line)]] | wt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 79.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPA]] | +0.64 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[SLC25A28]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PML]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[USF1]] | +0.56 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[UNC93B1]] | +0.55 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[ILF2]] | +0.55 | +0.33 / +0.58 | both halves | 1e-04 |  |
| [[HLA-C]] | +0.54 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LRP10]] | +0.53 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ATG9A]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[HECA]] | +0.50 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[ACAA1]] | +0.49 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[CD164]] | +0.49 | +0.39 / +0.58 | both halves | 5e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS9]] | -0.58 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[THUMPD2]] | -0.56 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[ACBD6]] | -0.56 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[SMIM30]] | -0.53 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[ESF1]] | -0.53 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[CCDC43]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ESD]] | -0.50 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[CEP290]] | -0.49 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[SLC25A43]] | -0.49 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[SHPRH]] | -0.47 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[CWC22]] | -0.47 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[RUFY1]] | -0.47 | -0.55 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises GTPBP1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.24× lower at baseline in the lines without OAS2 | 0.028 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[UBA7]] | B | UBA7 activity raises GTPBP1's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 1.37× lower at baseline in the lines without UBA7 | 0.041 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers GTPBP1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TRANK1]] | B | TRANK1 activity raises GTPBP1's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without TRANK1 | 0.061 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.420). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.2, 55.7); signed map (67.2, 33.6). **Vector** length 106, 29.4% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +0.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.4 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +6.9 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.6 |
|  | [[Ivermectin (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.5 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.5 | -1.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.4 | -4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -5.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.5 | -0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.4 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | GTP binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,705,742-38,738,299 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GP-1, HSPC018 |
| Gene groups (HGNC) | Translational GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [O00178](https://www.uniprot.org/uniprotkb/O00178) (GTP-binding protein 1):

> GTPase that plays a role in the elongation phase of protein synthesis by forming ternary complexes with GTP and aminoacyl-transfer RNAs (aa-tRNAs), and delivering aa-tRNAs to the ribosomal A site in a GTP-dependent manner. Is also able to deliver deacylated tRNA to the A site. Additionally, it is involved in RNA quality control; after GTP hydrolysis, which is not immediately followed by rapid peptide bond formation, GTPBP1 likely retains aa-tRNA in the A site and promotes exosomal degradation …

**Summary**, from NCBI Gene [9567](https://www.ncbi.nlm.nih.gov/gene/9567):

> This gene is upregulated by interferon-gamma and encodes a protein that is a member of the AGP11/GTPBP1 family of GTP-binding proteins. A structurally similar protein has been found in mouse, where disruption of the gene for that protein had no observable phenotype. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4669](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4669) · Entrez [9567](https://www.ncbi.nlm.nih.gov/gene/9567) · UniProt [O00178](https://www.uniprot.org/uniprotkb/O00178) · Ensembl [ENSG00000100226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100226)

## Data

Gene col 1897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1897); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1897]; `tensor/DDL_lfc|DDL_z.npy` [1897]; `embed/gene_vectors.npy` [1897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1897 or target_col == 1897). Every well: [[GTPBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTPBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
