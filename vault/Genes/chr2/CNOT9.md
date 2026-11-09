---
symbol: "CNOT9"
type: "gene"
col: 6898
ensembl_id: "ENSG00000144580"
name: "CCR4-NOT transcription complex subunit 9"
location: "2q35"
module: 6
arm: "+"
pooled_cpm: 56.01
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CNOT9

*CCR4-NOT transcription complex subunit 9* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.91× (z +12.0, q 3e-30, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.580× (z -10.1, q 3e-21, down in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.744× (z -7.8, q 1e-12, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTBP]] (+0.64, fdr 1e-05), [[C4orf46]] (+0.64, fdr 2e-05), [[CENPM]] (+0.62, fdr 1e-05); moves opposite to [[EIF1]] (-0.55, fdr 2e-05), [[SPTAN1]] (-0.52, fdr 4e-05), [[SHC2]] (-0.50, fdr 8e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6898.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.91×** | +12.0 | 3e-30 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.27×** | +11.5 | 6e-28 | 44/49 (HT-29, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +8.7 | 5e-16 | 33/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.26×** | +7.9 | 6e-13 | 36/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +6.9 | 7e-10 | 31/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +5.9 | 5e-07 | 32/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.31×** | +4.7 | 2e-04 | 27/48 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +4.1 | 0.002 | 24/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +4.0 | 0.005 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.20× | +3.2 | 0.085 | 12/49 (NCI-H460, SNU-423, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6898.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.580×** | -10.1 | 3e-21 | 38/49 (H4, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.584×** | -9.6 | 2e-19 | 34/44 (A549, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.744×** | -7.8 | 1e-12 | 41/48 (NCI-H2347, LS 180, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.795×** | -4.3 | 0.003 | 23/48 (COLO 205, NCI-H2347, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.806×** | -4.0 | 0.006 | 22/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.758×** | -3.7 | 0.021 | 18/48 (Hs 766T, HCT15, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.826×** | -3.6 | 0.027 | 19/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.830×** | -3.5 | 0.033 | 19/48 (SNU-423, HCT15, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.879× | -3.4 | 0.034 | 18/48 (A-427, A-172, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.833×** | -3.4 | 0.034 | 18/48 (SW 1271, AN3 CA, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.845× | -3.2 | 0.080 | 6/48 (SW 1271, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 63.0 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +16.4) | — |
| [[HT-29 (line)]] | alt | 36.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.10× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -12.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 44.5 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -13.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 64.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -10.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 43.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 54.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 53.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.48× (z +9.8) | — |
| [[LoVo (line)]] | wt | 38.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.40× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 85.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -14.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 58.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 58.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0556× (z -22.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 70.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -13.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 65.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.400× (z -9.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 67.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -10.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 55.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 56.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 45.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0533× (z -21.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 81.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 56.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.281× (z -9.5) |
| [[SNU-1 (line)]] | wt | 74.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -12.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 70.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.357× (z -8.6) |
| [[A498 (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTBP]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[C4orf46]] | +0.64 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[CENPM]] | +0.62 | +0.49 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[AUNIP]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SASS6]] | +0.61 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[POLA2]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[RFC4]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[RAD54L]] | +0.60 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[NCAPD3]] | +0.60 | +0.67 / +0.62 | both halves | 7e-06 | same gene group |
| [[SNRNP40]] | +0.60 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[RFC2]] | +0.59 | +0.51 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[NIF3L1]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1]] | -0.55 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[SPTAN1]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SHC2]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CNOT9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.4, -46.1); signed map (-38.4, -41.2). **Vector** length 83.8, 19.3% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Translesion synthesis by REV1* (reactome, mean cos +0.51 to 6); *Translesion synthesis by POLI* (reactome, mean cos +0.51 to 6); *Translesion synthesis by POLK* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +11.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Gemcitabine (drug)]] 5 µM |  | +1.5 | +0.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -7.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | CCR4-NOT transcription complex subunit 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,568,580-218,597,080 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RCD1, RCD1+, CT129, CAF40; previously RQCD1 |
| Gene groups (HGNC) | CCR4-NOT transcription complex; Armadillo like helical domain containing |
| Hallmark sets | E2F_TARGETS |
| Reactome | 10 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92600](https://www.uniprot.org/uniprotkb/Q92600) (CCR4-NOT transcription complex subunit 9):

> Component of the CCR4-NOT complex which is one of the major cellular mRNA deadenylases and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. Additional complex functions may be a consequence of its influence on mRNA expression. Involved in down-regulation of MYB- and JUN-dependent transcription. May play a role in cell differentiation (By similarity). …

**Summary**, from NCBI Gene [9125](https://www.ncbi.nlm.nih.gov/gene/9125):

> This gene encodes a member of the highly conserved RCD1 protein family. The encoded protein is a transcriptional cofactor and a core protein of the CCR4-NOT complex. It may be involved in signal transduction as well as retinoic acid-regulated cell differentiation and development. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:10445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10445) · Entrez [9125](https://www.ncbi.nlm.nih.gov/gene/9125) · UniProt [Q92600](https://www.uniprot.org/uniprotkb/Q92600) · Ensembl [ENSG00000144580](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144580)

## Data

Gene col 6898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6898); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6898]; `tensor/DDL_lfc|DDL_z.npy` [6898]; `embed/gene_vectors.npy` [6898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6898 or target_col == 6898). Every well: [[CNOT9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNOT9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
