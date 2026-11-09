---
symbol: "SPATA2L"
type: "gene"
col: 8190
ensembl_id: "ENSG00000158792"
name: "spermatogenesis associated 2 like"
location: "16q24.3"
module: 218
arm: "+"
pooled_cpm: 7.07
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/218"]
generated_by: "tahoemap"
---

# SPATA2L

*spermatogenesis associated 2 like* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.45× (z +10.7, q 1e-23, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.643× (z -5.1, q 1e-04, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF16]] (+0.66, fdr 7e-06), [[MIDN]] (+0.65, fdr 1e-05), [[FAM89B]] (+0.65, fdr 1e-05); moves opposite to [[DECR1]] (-0.67, fdr 3e-05), [[NNT]] (-0.63, fdr 2e-05), [[DERA]] (-0.63, fdr 3e-05).
> It is in [[Module 218]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EFEMP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +10.7 | 1e-23 | 37/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +9.6 | 3e-19 | 33/47 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +8.5 | 4e-15 | 34/47 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +8.4 | 6e-15 | 30/46 (SW1417, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +5.7 | 1e-06 | 20/47 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.40×** | +5.7 | 1e-06 | 18/43 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +5.2 | 2e-05 | 21/43 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.49×** | +4.6 | 3e-04 | 17/45 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.093 | 5/42 (SW480, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Decitabine (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.093 | 5/44 (BT-474, NCI-H2030, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8190.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -5.1 | 1e-04 | 22/44 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.684×** | -5.0 | 1e-04 | 20/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.645×** | -5.0 | 1e-04 | 20/45 (HS-578T, A498, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.481×** | -4.6 | 8e-04 | 20/45 (MIA PaCa-2, HCT15, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.765×** | -4.5 | 8e-04 | 19/46 (HS-578T, HOP62, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.677×** | -4.3 | 0.002 | 11/46 (NCI-H2030, A549, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -4.2 | 0.002 | 17/48 (hTERT-HPNE, NCI-H2030, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.510×** | -4.2 | 0.002 | 12/38 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -3.9 | 0.005 | 11/41 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.791×** | -3.7 | 0.010 | 12/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.811×** | -3.5 | 0.025 | 13/46 (RPMI-7951, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.755×** | -3.3 | 0.040 | 18/31 (NCI-H2030, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.760×** | -3.3 | 0.047 | 13/47 (SW48, NCI-H23, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.745×** | -3.2 | 0.049 | 12/19 (A498, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | **0.828×** | -3.2 | 0.059 | 5/47 (NCI-H661, SW480, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.765×** | -3.1 | 0.078 | 15/45 (NCI-H23, A-172, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 9.56 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0351× (z -15.6) |
| [[CFPAC-1 (line)]] | alt | 7.69 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.185× (z -8.5) |
| [[HOP62 (line)]] | alt | 7.11 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0650× (z -12.2) |
| [[HT-29 (line)]] | alt | 8.35 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0868× (z -11.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 7.05 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0647× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0492× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 4.09 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0750× (z -10.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 5.46 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +10.3) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW 900 (line)]] | alt | 4.64 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0662× (z -8.5) |
| [[A-172 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF16]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MIDN]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.65 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[PRKCD]] | +0.63 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[METRNL]] | +0.63 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ASL]] | +0.62 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SYP]] | +0.62 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[ORAI1]] | +0.61 | +0.37 / +0.66 | both halves | 7e-05 |  |
| [[PLIN3]] | +0.61 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SNAPC2]] | +0.61 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[DUSP2]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CLIP2]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.67 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[NNT]] | -0.63 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[DERA]] | -0.63 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[RCN1]] | -0.61 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[C5orf15]] | -0.61 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[FUBP1]] | -0.60 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[SUMO3]] | -0.59 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[RAB11FIP2]] | -0.58 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[HFE]] | -0.58 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[SETD7]] | -0.58 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[VPS52]] | -0.57 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[FUCA2]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFEMP1]] | B | EFEMP1 activity lowers SPATA2L's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.16× higher at baseline in the lines without EFEMP1 | 0.058 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[TOP2A]] | B | TOP2A activity raises SPATA2L's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers SPATA2L's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 218]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.4, 1.4); signed map (-26.8, 16.2). **Vector** length 84.0, 16.2% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +10.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +8.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +9.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.4 | +0.1 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | -1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.3 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -2.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,696,357-89,701,705 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC26885, tamo; previously C16orf76 |
| Matched by | ensembl_id |

UniProt [Q8IUW3](https://www.uniprot.org/uniprotkb/Q8IUW3) carries no function annotation.

**Summary**, from NCBI Gene [124044](https://www.ncbi.nlm.nih.gov/gene/124044):

> Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28393) · Entrez [124044](https://www.ncbi.nlm.nih.gov/gene/124044) · UniProt [Q8IUW3](https://www.uniprot.org/uniprotkb/Q8IUW3) · Ensembl [ENSG00000158792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158792)

## Data

Gene col 8190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8190); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8190]; `tensor/DDL_lfc|DDL_z.npy` [8190]; `embed/gene_vectors.npy` [8190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8190 or target_col == 8190). Every well: [[SPATA2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
