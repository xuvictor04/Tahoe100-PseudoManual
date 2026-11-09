---
symbol: "NUDT6"
type: "gene"
col: 10026
ensembl_id: "ENSG00000170917"
name: "nudix hydrolase 6"
location: "4q28.1"
module: 16
arm: "+"
pooled_cpm: 5.37
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# NUDT6

*nudix hydrolase 6* — 4q28.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.41× (z +9.2, q 1e-17, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +8.3, q 3e-14, up in 23 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.545× (z -6.6, q 2e-08, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMACHC]] (+0.64, fdr 1e-05), [[DUSP19]] (+0.59, fdr 7e-06), [[ETAA1]] (+0.56, fdr 3e-05); moves opposite to [[PCYT1A]] (-0.53, fdr 6e-05), [[TPD52L2]] (-0.51, fdr 2e-05), [[SAMD4B]] (-0.49, fdr 2e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +9.2 | 1e-17 | 3/10 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +8.3 | 3e-14 | 23/38 (SNU-423, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +8.2 | 5e-14 | 30/46 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +7.2 | 9e-11 | 24/46 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.89×** | +6.9 | 4e-10 | 16/24 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +6.7 | 2e-09 | 26/44 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +6.3 | 2e-08 | 18/46 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +5.8 | 3e-07 | 16/44 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +5.8 | 3e-07 | 12/46 (A549, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +5.7 | 5e-07 | 3/12 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.2 | 1e-05 | 15/34 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +5.0 | 2e-05 | 16/45 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.6 | 2e-04 | 11/42 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.5 | 2e-04 | 15/46 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.14×** | +4.3 | 5e-04 | 8/41 (A-172, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.017 | 9/41 (SW480, HT-29, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.043 | 3/26 (Hs 766T, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.0 | 0.093 | 6/37 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.545×** | -6.6 | 2e-08 | 23/45 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.553×** | -6.5 | 3e-08 | 20/46 (H4, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.677×** | -4.3 | 0.004 | 17/46 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.738× | -3.3 | 0.12 | 9/43 (LoVo, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.749× | -3.2 | 0.18 | 14/36 (HOP62, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 7.23 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM 0.0750× (z -8.5) |
| [[H4 (line)]] | wt | 6.94 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0412× (z -8.8) |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -8.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 3.51 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0795× (z -8.5) |
| [[A-172 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMACHC]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[DUSP19]] | +0.59 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ETAA1]] | +0.56 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[DHFR2]] | +0.56 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[OSGEPL1]] | +0.55 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PUM2]] | +0.53 | +0.13 / +0.44 | ⚠ not reproduced | 0.002 |  |
| [[HERPUD2-AS1]] | +0.51 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ATF7IP]] | +0.51 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[SCAF8]] | +0.50 | +0.35 / +0.30 | both halves | 2e-04 |  |
| [[DPY19L2P2-1]] | +0.49 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[KAT6A]] | +0.49 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[NUDT7]] | +0.49 | +0.47 / +0.54 | both halves | 2e-05 | same gene group; STRING 472 |
| [[COQ2]] | +0.48 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCYT1A]] | -0.53 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[TPD52L2]] | -0.51 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[SAMD4B]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[TANGO2]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[HOOK3]] | -0.47 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[TAF13]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[DHDDS]] | -0.46 | -0.63 / -0.29 | both halves | 2e-04 |  |
| [[RABGEF1]] | -0.46 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[CHFR]] | -0.46 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[MYO9B]] | -0.45 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[SGSM3]] | -0.45 | -0.65 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[SS18L1]] | -0.45 | -0.63 / -0.26 | both halves | 3e-04 |  |
| [[MROH1]] | -0.45 | -0.38 / -0.53 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NUDT6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.365). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.0, 20.5); signed map (10.1, -39.9). **Vector** length 39.4, 4.29% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +9.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.0 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +2.0 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.1 — chr4:122,888,697-122,922,968 (-) |
| Ensembl biotype | protein_coding |
| Also known as | gfg-1, gfg, FGF2AS, FGF-AS |
| Gene groups (HGNC) | Nudix hydrolase family |
| Matched by | ensembl_id |

**Function**, from UniProt [P53370](https://www.uniprot.org/uniprotkb/P53370) (Nudix hydrolase 6):

> Mediates the hydrolysis of some nucleoside diphosphate derivatives, such as NADH and FAD (in vitro). May contribute to the regulation of cell proliferation.

**Summary**, from NCBI Gene [11162](https://www.ncbi.nlm.nih.gov/gene/11162):

> This gene overlaps and lies on the opposite strand from FGF2 gene, and is thought to be the FGF2 antisense gene. The two genes are independently transcribed, and their expression shows an inverse relationship, suggesting that this antisense transcript may regulate FGF2 expression. This gene has also been shown to have hormone-regulatory and antiproliferative actions in the pituitary that are independent of FGF2 expression. Alternatively spliced transcript variants encoding different isoforms …

**Accessions** — [HGNC:8053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8053) · Entrez [11162](https://www.ncbi.nlm.nih.gov/gene/11162) · UniProt [P53370](https://www.uniprot.org/uniprotkb/P53370) · Ensembl [ENSG00000170917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170917)

## Data

Gene col 10026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10026); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10026]; `tensor/DDL_lfc|DDL_z.npy` [10026]; `embed/gene_vectors.npy` [10026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10026 or target_col == 10026). Every well: [[NUDT6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
