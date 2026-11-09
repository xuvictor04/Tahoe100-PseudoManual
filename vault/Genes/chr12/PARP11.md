---
symbol: "PARP11"
type: "gene"
col: 3203
ensembl_id: "ENSG00000111224"
name: "poly(ADP-ribose) polymerase family member 11"
location: "12p13.32"
module: 23
arm: "+"
pooled_cpm: 26.24
n_lines_expressing: 47
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PARP11

*poly(ADP-ribose) polymerase family member 11* — 12p13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +5.9, q 2e-06, up in 21 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 1.70×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.648× (z -6.7, q 1e-08, down in 28 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.701× (z -5.5, q 4e-06, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF846]] (+0.51, fdr 1e-04), [[BORCS7]] (+0.51, fdr 5e-04), [[ZNF596]] (+0.50, fdr 1e-04); moves opposite to [[GMDS]] (-0.53, fdr 1e-04), [[ANKS6]] (-0.44, fdr 2e-04), [[RRP1B]] (-0.42, fdr 4e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[KLF3-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3203.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 1.70×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.9 | 2e-06 | 21/44 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.21×** | +4.2 | 0.009 | 18/45 (J82, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.2 | 0.20 | 19/45 (HT-29, KATO III, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.48× | +3.2 | 0.20 | 6/44 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.23× | +3.0 | 0.26 | 13/44 (HS-578T, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3203.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.648×** | -6.7 | 1e-08 | 28/43 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -6.4 | 5e-08 | 31/45 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.659×** | -6.2 | 1e-07 | 25/44 (H4, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.685×** | -5.6 | 3e-06 | 20/31 (H4, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.701×** | -5.5 | 4e-06 | 31/44 (SNU-1, SW 1271, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.707×** | -5.4 | 7e-06 | 24/45 (H4, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.728×** | -4.9 | 7e-05 | 23/44 (A549, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.755×** | -4.0 | 0.004 | 20/39 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.615×** | -3.9 | 0.005 | 18/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.617×** | -3.9 | 0.005 | 17/45 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.837× | -3.9 | 0.005 | 19/44 (PANC-1, HOP62, …) | top dose only | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.637×** | -3.6 | 0.012 | 13/43 (A549, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.807×** | -3.3 | 0.040 | 16/45 (C-33 A, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.809×** | -3.3 | 0.043 | 15/45 (SW480, HT-29, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.745×** | -3.3 | 0.043 | 14/45 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.819×** | -3.1 | 0.069 | 14/44 (LOX-IMVI, SW48, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.814×** | -3.0 | 0.094 | 10/45 (NCI-H23, C32, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 57.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0797× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SNU-1 (line)]] | wt | 43.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.243× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 49.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SW480 (line)]] | alt | 53.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HCT15 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[HT-29 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[LoVo (line)]] | wt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[NCI-H23 (line)]] | alt | 72.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[RKO (line)]] | wt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0823× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SNU-423 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SW1417 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[A-172 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF846]] | +0.51 | +0.35 / +0.37 | both halves | 1e-04 |  |
| [[BORCS7]] | +0.51 | +0.59 / +0.24 | both halves | 5e-04 |  |
| [[ZNF596]] | +0.50 | +0.41 / +0.36 | both halves | 1e-04 |  |
| [[SPATA1]] | +0.49 | +0.37 / +0.32 | both halves | 2e-04 |  |
| [[HECTD2]] | +0.48 | +0.38 / +0.27 | both halves | 3e-04 |  |
| [[AP4S1]] | +0.48 | +0.29 / +0.31 | both halves | 3e-04 |  |
| [[ZKSCAN7-AS1]] | +0.48 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[FRS2]] | +0.47 | +0.39 / +0.30 | both halves | 2e-04 |  |
| [[THBS4]] | +0.46 | +0.38 / +0.30 | both halves | 2e-04 |  |
| [[ZNF189]] | +0.46 | +0.38 / +0.36 | both halves | 9e-05 |  |
| [[PIGC]] | +0.46 | +0.41 / +0.29 | both halves | 2e-04 |  |
| [[STX17-DT]] | +0.46 | +0.29 / +0.37 | both halves | 2e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMDS]] | -0.53 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[ANKS6]] | -0.44 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[RRP1B]] | -0.42 | -0.29 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF3-AS1]] | C | PARP11 activity raises KLF3-AS1's level | lines that do not express PARP11 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without PARP11 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NECAB2, FAT3, ENSG00000205890; its own permutation p |
| [[FBXO8]] | C | PARP11 activity lowers FBXO8's level | lines that do not express PARP11 (3) vs lines expressing it (47) | 1.47× higher at baseline in the lines without PARP11 | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NECAB2, FAT3, ENSG00000205890 |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.419). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (8.3, 22.7); signed map (29.5, -15.5). **Vector** length 65.7, 11.0% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +4.5 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | -1.8 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +0.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase family member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.32 — chr12:3,791,047-3,873,448 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARTD11; previously C12orf6 |
| Gene groups (HGNC) | Poly(ADP-ribose) polymerases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR21](https://www.uniprot.org/uniprotkb/Q9NR21) (Protein mono-ADP-ribosyltransferase PARP11):

> Mono-ADP-ribosyltransferase that mediates mono-ADP-ribosylation of target proteins. Plays a role in nuclear envelope stability and nuclear remodeling during spermiogenesis (By similarity). Inhibits the type I interferon activated signaling pathway. Mechanistically, mono-ADP-ribosylates beta-TrCP/BTRC to promote IFNAR1 ubiquitination and protect BTRC from ubiquitin-proteasome degradation. Additionally, acts as an antiviral factor by cooperating with PARP12 to suppress Zika virus replication, …

**Summary**, from NCBI Gene [57097](https://www.ncbi.nlm.nih.gov/gene/57097):

> Enables NAD+ poly-ADP-ribosyltransferase activity and NAD+-protein mono-ADP-ribosyltransferase activity. Involved in protein auto-ADP-ribosylation. Located in nuclear body and nuclear envelope. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1186) · Entrez [57097](https://www.ncbi.nlm.nih.gov/gene/57097) · UniProt [Q9NR21](https://www.uniprot.org/uniprotkb/Q9NR21) · Ensembl [ENSG00000111224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111224)

## Data

Gene col 3203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3203); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3203]; `tensor/DDL_lfc|DDL_z.npy` [3203]; `embed/gene_vectors.npy` [3203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3203 or target_col == 3203). Every well: [[PARP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
