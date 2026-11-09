---
symbol: "DHRS4"
type: "gene"
col: 8060
ensembl_id: "ENSG00000157326"
name: "dehydrogenase/reductase 4"
location: "14q11.2"
module: 137
arm: "+"
pooled_cpm: 4.3
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# DHRS4

*dehydrogenase/reductase 4* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.59× (z +11.9, q 8e-30, up in 19 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.68× (z +6.8, q 1e-09, up in 18 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.327× (z -10.4, q 2e-22, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAIM]] (+0.75, fdr 1e-05), [[IDNK]] (+0.69, fdr 1e-05), [[ANGEL2]] (+0.68, fdr 1e-04); moves opposite to [[EHD4]] (-0.62, fdr 1e-04), [[FLNB]] (-0.57, fdr 4e-04), [[GNAI2]] (-0.57, fdr 0.002, ⚠ not reproduced), [[SH3GL3]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.59×** | +11.9 | 8e-30 | 19/22 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +11.2 | 1e-26 | 7/8 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +9.8 | 3e-20 | 11/11 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +6.8 | 1e-09 | 18/45 (CFPAC-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.7 | 2e-06 | 14/23 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +4.0 | 0.006 | 10/26 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.7 | 0.019 | 11/40 (HEC-1-A, NCI-H1573, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.085 | 9/46 (NCI-H2030, A-172, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | 1.27× | +3.2 | 0.10 | 6/45 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.327×** | -10.4 | 2e-22 | 38/46 (SNU-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.370×** | -9.2 | 7e-18 | 40/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.371×** | -9.2 | 7e-18 | 34/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.430×** | -7.8 | 6e-13 | 33/46 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.555×** | -7.7 | 1e-12 | 28/38 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.404×** | -4.4 | 0.001 | 17/45 (SW480, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.720×** | -4.3 | 0.001 | 18/44 (SW480, C-33 A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.641×** | -4.1 | 0.003 | 14/44 (SNU-423, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.651×** | -4.0 | 0.004 | 15/38 (hTERT-HPNE, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.663×** | -3.8 | 0.008 | 14/46 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.699×** | -3.3 | 0.046 | 13/45 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.707×** | -3.2 | 0.061 | 14/36 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 5.50 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0861× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.212× (z -8.9) |
| [[SW480 (line)]] | alt | 5.34 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -12.4) |
| [[HOP62 (line)]] | alt | 3.97 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0966× (z -9.1) |
| [[LoVo (line)]] | wt | 5.57 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.152× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 4.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.4) |
| [[SNU-1 (line)]] | wt | 7.07 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0253× (z -10.8) |
| [[A-172 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAIM]] | +0.75 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[IDNK]] | +0.69 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ANGEL2]] | +0.68 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[GTF3C6]] | +0.66 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[HOXB7]] | +0.65 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[MAIP1]] | +0.63 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[HFE]] | +0.63 | +0.53 / +0.38 | both halves | 7e-05 |  |
| [[AP5M1]] | +0.63 | +0.43 / +0.27 | both halves | 3e-04 |  |
| [[GAS2]] | +0.62 | +0.43 / +0.31 | both halves | 2e-04 |  |
| [[RAB21]] | +0.61 | +0.39 / +0.39 | both halves | 6e-05 |  |
| [[RNF146]] | +0.61 | +0.40 / +0.29 | both halves | 2e-04 |  |
| [[PNISR-AS1]] | +0.61 | +0.40 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | -0.62 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[FLNB]] | -0.57 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[GNAI2]] | -0.57 | -0.37 / -0.12 | ⚠ not reproduced | 0.002 | pathway: Signaling by Nuclear Receptors |
| [[SH3GL3]] | -0.56 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[DNAAF3]] | -0.56 | -0.35 / -0.26 | both halves | 4e-04 |  |
| [[CMIP]] | -0.55 | -0.42 / -0.29 | both halves | 3e-04 |  |
| [[CADM4]] | -0.55 | -0.34 / -0.23 | both halves | 5e-04 |  |
| [[HIVEP3]] | -0.55 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[FCHO1]] | -0.55 | -0.35 / -0.28 | both halves | 3e-04 |  |
| [[EPN2]] | -0.54 | -0.55 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[GDPD5]] | -0.54 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[SPATA2L]] | -0.54 | -0.52 / -0.24 | both halves | 5e-04 |  |
| [[ARHGEF10]] | -0.54 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[ACTG1]] | -0.54 | -0.44 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DHRS4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DHRS4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.693). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-2.9, 13.5); signed map (24.5, -23.0). **Vector** length 49.3, 6.21% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.7 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.0 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -7.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | -9.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.4 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.0 | -10.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -4.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Baicalin (drug)]] 5 µM |  | -0.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,953,734-23,969,279 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCAD-SRL, SDR-SRL, humNRDR, FLJ11008, SDR25C2 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 5 pathways, smallest: RA biosynthesis pathway; Signaling by Retinoic Acid; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTZ2](https://www.uniprot.org/uniprotkb/Q9BTZ2) (Dehydrogenase/reductase SDR family member 4):

> NADPH-dependent oxidoreductase which catalyzes the reduction of a variety of compounds bearing carbonyl groups including ketosteroids, alpha-dicarbonyl compounds, aldehydes, aromatic ketones and quinones. Reduces 3-ketosteroids and benzil into 3beta-hydroxysteroids and R-benzoin, respectively, in contrast to the stereoselectivity of non-primate DHRS4s which produce 3alpha-hydroxysteroids and S-benzoin. Displays low activity toward all-trans-retinal and no activity toward 9-cis-retinal as …

**Summary**, from NCBI Gene [10901](https://www.ncbi.nlm.nih.gov/gene/10901):

> Enables identical protein binding activity; oxidoreductase activity, acting on NAD(P)H, quinone or similar compound as acceptor; and oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor. Involved in ketone metabolic process; positive regulation of reactive oxygen species metabolic process; and steroid metabolic process. Located in nucleus and peroxisomal membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16985) · Entrez [10901](https://www.ncbi.nlm.nih.gov/gene/10901) · UniProt [Q9BTZ2](https://www.uniprot.org/uniprotkb/Q9BTZ2) · Ensembl [ENSG00000157326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157326)

## Data

Gene col 8060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8060); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8060]; `tensor/DDL_lfc|DDL_z.npy` [8060]; `embed/gene_vectors.npy` [8060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8060 or target_col == 8060). Every well: [[DHRS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
