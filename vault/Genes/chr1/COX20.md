---
symbol: "COX20"
type: "gene"
col: 12775
ensembl_id: "ENSG00000203667"
name: "cytochrome c oxidase assembly factor COX20"
location: "1q44"
module: 52
arm: "-"
pooled_cpm: 45.33
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# COX20

*cytochrome c oxidase assembly factor COX20* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.29× (z +9.4, q 2e-18, up in 44 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 4.66×, RKO 4.06×, HT-29 3.73×, HS-578T 3.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 3.35×, HT-29 3.38×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 3.14×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.488× (z -8.1, q 3e-13, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (71 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 29 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00938]] (+0.52, fdr 8e-05), [[ACVR2A]] (+0.46, fdr 1e-04), [[MRPS30-DT]] (+0.45, fdr 4e-04); moves opposite to [[GOLGA3]] (-0.48, fdr 8e-05), [[EP400]] (-0.47, fdr 8e-04, ⚠ not reproduced), [[CDRT4]] (-0.47, fdr 7e-05), [[MIER2]] (-0.47, fdr 2e-04).
> It sits in the **-** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12775.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 4.66×, RKO 4.06×, HT-29 3.73×, HS-578T 3.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 3.35×, HT-29 3.38×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 3.14×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +9.4 | 2e-18 | 44/47 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +7.9 | 1e-12 | 38/40 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +6.6 | 7e-09 | 41/47 (NCI-H1573, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +5.9 | 4e-07 | 31/43 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.55×** | +5.0 | 6e-05 | 35/47 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12775.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.488×** | -8.1 | 3e-13 | 43/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.617×** | -7.7 | 3e-12 | 34/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.554×** | -6.7 | 5e-09 | 37/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.608×** | -5.6 | 3e-06 | 36/48 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.531×** | -3.7 | 0.020 | 27/47 (SK-MEL-2, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.748× | -3.3 | 0.10 | 25/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 61.7 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -14.4) |
| [[SHP-77 (line)]] | alt | 46.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -10.0) |
| [[HS-578T (line)]] | alt | 44.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.309× (z -8.6) |
| [[HT-29 (line)]] | alt | 32.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 39.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 49.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.2) |
| [[A-427 (line)]] | wt | 65.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 76.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -8.8) |
| [[COLO 205 (line)]] | alt | 38.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -9.4) |
| [[H4 (line)]] | wt | 49.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -8.7) |
| [[LS 180 (line)]] | wt | 61.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 56.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 49.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.14× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +9.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 64.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +10.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 55.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 70.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.2) |
| [[SW48 (line)]] | wt | 52.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.9) |
| [[A-172 (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00938]] | +0.52 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[ACVR2A]] | +0.46 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[MRPS30-DT]] | +0.45 | +0.41 / +0.25 | both halves | 4e-04 |  |
| [[SDHAF4]] | +0.45 | +0.19 / +0.47 | ⚠ not reproduced | 9e-04 | same gene group; pathway: Aerobic respiration and respiratory electron transport |
| [[SINHCAF]] | +0.45 | +0.36 / +0.30 | both halves | 2e-04 |  |
| [[ZNF670]] | +0.45 | +0.29 / +0.43 | both halves | 3e-04 |  |
| [[ZNRF2P2]] | +0.44 | +0.33 / +0.35 | both halves | 1e-04 |  |
| [[THEM4]] | +0.44 | +0.04 / +0.45 | ⚠ not reproduced | 0.005 |  |
| [[PIAS2]] | +0.43 | +0.51 / +0.30 | both halves | 2e-04 |  |
| [[TRIM66]] | +0.43 | +0.18 / +0.39 | ⚠ not reproduced | 1e-03 |  |
| [[FZD3]] | +0.43 | +0.35 / +0.20 | ⚠ not reproduced | 8e-04 |  |
| [[ELAPOR2]] | +0.43 | +0.42 / +0.30 | both halves | 2e-04 |  |
| [[CMC1]] | +0.43 | +0.32 / +0.49 | both halves | 2e-04 | same gene group; pathway: Aerobic respiration and respiratory electron transport |
| [[POU2F1]] | +0.43 | +0.47 / +0.25 | both halves | 4e-04 |  |
| [[VGLL4]] | +0.42 | +0.39 / +0.31 | both halves | 2e-04 |  |
| [[PIGX]] | +0.42 | +0.29 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA3]] | -0.48 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[EP400]] | -0.47 | -0.20 / -0.46 | ⚠ not reproduced | 8e-04 |  |
| [[CDRT4]] | -0.47 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[MIER2]] | -0.47 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[PDPK1]] | -0.47 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[NPIPB14P]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[DPH7]] | -0.46 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[GOLGA2]] | -0.46 | -0.39 / -0.26 | both halves | 4e-04 |  |
| [[FAM98A]] | -0.46 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[MINAR1]] | -0.46 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[TTLL11]] | -0.46 | -0.39 / -0.37 | both halves | 7e-05 |  |
| [[PDXDC2P-NPIPB14P]] | -0.44 | -0.24 / -0.37 | both halves | 5e-04 |  |
| [[PDXDC1]] | -0.44 | -0.24 / -0.40 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises COX20's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.393). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (18.9, -34.6); signed map (-5.6, -10.2). **Vector** length 64.0, 15.1% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | -0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +0.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | +0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -8.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -3.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -0.9 | +0.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor COX20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:244,835,616-244,845,057 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ43269; previously FAM36A |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5RI15](https://www.uniprot.org/uniprotkb/Q5RI15) (Cytochrome c oxidase assembly protein COX20, mitochondrial):

> Essential for the assembly of the mitochondrial respiratory chain complex IV (CIV), also known as cytochrome c oxidase. Acts as a chaperone in the early steps of cytochrome c oxidase subunit II (MT-CO2/COX2) maturation, stabilizing the newly synthesized protein and presenting it to metallochaperones SCO1/2 which in turn facilitates the incorporation of the mature MT-CO2/COX2 into the assembling CIV holoenzyme.

**Summary**, from NCBI Gene [116228](https://www.ncbi.nlm.nih.gov/gene/116228):

> This gene encodes a protein that plays a role in the assembly of cytochrome C oxidase, an important component of the respiratory pathway. It contains two transmembrane helices and localizes to the mitochondrial membrane. Mutations in this gene can cause mitochondrial complex IV deficiency, which results in ataxia and muscle hypotonia. There are multiple pseudogenes for this gene. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:26970](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26970) · Entrez [116228](https://www.ncbi.nlm.nih.gov/gene/116228) · UniProt [Q5RI15](https://www.uniprot.org/uniprotkb/Q5RI15) · Ensembl [ENSG00000203667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203667)

## Data

Gene col 12775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12775); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12775]; `tensor/DDL_lfc|DDL_z.npy` [12775]; `embed/gene_vectors.npy` [12775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12775 or target_col == 12775). Every well: [[COX20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
