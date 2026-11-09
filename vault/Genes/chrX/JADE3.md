---
symbol: "JADE3"
type: "gene"
col: 2227
ensembl_id: "ENSG00000102221"
name: "jade family PHD finger 3"
location: "Xp11.3"
module: 143
arm: "+"
pooled_cpm: 39.16
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# JADE3

*jade family PHD finger 3* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +11.2, q 2e-26, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.586× (z -5.5, q 3e-05, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP11C]] (+0.69, fdr 7e-06), [[CCNJ]] (+0.64, fdr 3e-05), [[SFMBT1]] (+0.63, fdr 1e-05); moves opposite to [[IFT172]] (-0.64, fdr 4e-05), [[MED23]] (-0.59, fdr 1e-05), [[MAP3K13]] (-0.58, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NINL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +11.2 | 2e-26 | 33/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.5 | 2e-11 | 30/47 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +7.0 | 7e-10 | 26/48 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 1e-04 | 29/47 (SW480, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +4.4 | 0.001 | 20/47 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.006 | 18/48 (CFPAC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.6 | 0.018 | 18/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.20×** | +3.6 | 0.018 | 16/48 (Panc 03.27, SNU-423, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.018 | 11/48 (HEC-1-A, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.018 | 17/47 (Hs 766T, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.046 | 20/48 (LS 180, H4, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.070 | 11/47 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.17× | +3.1 | 0.074 | 14/47 (A-172, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.0 | 0.095 | 15/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2227.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.586×** | -5.5 | 3e-05 | 26/48 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.780×** | -4.9 | 3e-04 | 24/48 (A549, A498, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.804×** | -4.3 | 0.003 | 21/47 (LoVo, SW480, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.761×** | -3.8 | 0.019 | 12/46 (SW480, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -3.2 | 0.15 | 9/48 (SW480, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 42.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.474× (z -8.5) |
| [[A549 (line)]] | wt | 64.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0600× (z -28.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 55.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 32.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +12.5) | — |
| [[NCI-H2347 (line)]] | alt | 28.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 46.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.6) | — |
| [[RKO (line)]] | wt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 65.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP11C]] | +0.69 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[CCNJ]] | +0.64 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[SFMBT1]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[NACC2]] | +0.63 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[DPY19L1P1]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[HDGFL3]] | +0.60 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[ARSB]] | +0.59 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ARHGEF11]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[UBTF]] | +0.58 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[TCF12]] | +0.58 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[RCC2]] | +0.58 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[ATE1]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.64 | -0.65 / -0.43 | both halves | 4e-05 |  |
| [[MED23]] | -0.59 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[MAP3K13]] | -0.58 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.57 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ABCB9]] | -0.56 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[OSBPL7]] | -0.56 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[GUSBP1]] | -0.55 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[ZNF511]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[RCN3]] | -0.54 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[SNAPC3]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[UBE4A]] | -0.54 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[NPHP1]] | -0.53 | -0.33 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NINL]] | B | NINL activity raises JADE3's level | lines that do not express NINL (10) vs lines expressing it (40) | 1.03× lower at baseline in the lines without NINL | 0.095 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZIM2-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.6, 11.3); signed map (8.7, -3.9). **Vector** length 96.3, 20.9% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +11.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +7.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.2 | +4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.7 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +0.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -4.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +0.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -4.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | jade family PHD finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:46,912,276-47,061,242 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0215, JADE-3; previously PHF16 |
| Gene groups (HGNC) | PHD finger proteins; Jade family PHD fingers |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92613](https://www.uniprot.org/uniprotkb/Q92613) (Protein Jade-3):

> Scaffold subunit of some HBO1 complexes, which have a histone H4 acetyltransferase activity.

**Summary**, from NCBI Gene [9767](https://www.ncbi.nlm.nih.gov/gene/9767):

> This gene encodes a member of a family of large proteins containing PHD (plant homeo domain)-type zinc fingers. The encoded protein may be associated in a nuclear complex that functions in histone H4 acetylation. Alternative splicing results in multiple transcript variants encoding the same protein. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:22982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22982) · Entrez [9767](https://www.ncbi.nlm.nih.gov/gene/9767) · UniProt [Q92613](https://www.uniprot.org/uniprotkb/Q92613) · Ensembl [ENSG00000102221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102221)

## Data

Gene col 2227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2227); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2227]; `tensor/DDL_lfc|DDL_z.npy` [2227]; `embed/gene_vectors.npy` [2227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2227 or target_col == 2227). Every well: [[JADE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JADE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
