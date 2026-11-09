---
symbol: "NPIPB2"
type: "gene"
col: 13978
ensembl_id: "ENSG00000234719"
name: "nuclear pore complex interacting protein family member B2"
location: "16p13.13"
module: 35
arm: "+"
pooled_cpm: 5.37
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# NPIPB2

*nuclear pore complex interacting protein family member B2* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.34× (z +13.2, q 4e-37, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +12.0, q 1e-30, up in 29 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.457× (z -9.3, q 9e-18, down in 26 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.399× (z -5.7, q 4e-06, down in 15 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATE1OSP]] (+0.69, fdr 7e-06), [[LINC02951]] (+0.66, fdr 2e-05), [[C8orf44-SGK3]] (+0.66, fdr 1e-05); moves opposite to [[ATP5MC3]] (-0.53, fdr 7e-05, ⚠ ATP5MC3 in the vector space only through flagged drug-doses), [[THEM6]] (-0.52, fdr 5e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.34×** | +13.2 | 4e-37 | 4/9 (SW1417, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +12.0 | 1e-30 | 29/40 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +11.2 | 7e-27 | 23/41 (NCI-H2030, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +7.1 | 2e-10 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +6.8 | 1e-09 | 20/45 (SW48, H4, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +6.5 | 8e-09 | 10/27 (SW1417, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +6.4 | 2e-08 | 20/46 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.37×** | +5.2 | 1e-05 | 15/45 (A498, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.59×** | +5.2 | 1e-05 | 14/43 (A-172, H4, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.2 | 1e-05 | 18/39 (SW48, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +4.9 | 4e-05 | 14/46 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +4.9 | 5e-05 | 15/46 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.5 | 3e-04 | 8/27 (NCI-H460, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 4e-04 | 12/45 (J82, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.001 | 10/46 (A498, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.002 | 8/46 (A-172, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.010 | 10/39 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.037 | 5/46 (RKO, HEC-1-A, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.042 | 6/44 (PANC-1, HOP62, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.042 | 7/45 (A498, NCI-H661, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.20× | +3.0 | 0.069 | 3/46 (PANC-1, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13978.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.457×** | -9.3 | 9e-18 | 26/46 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.399×** | -5.7 | 4e-06 | 15/44 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.488×** | -4.4 | 0.002 | 13/38 (A498, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.681×** | -4.3 | 0.002 | 14/44 (NCI-H2347, PANC-1, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.509×** | -4.2 | 0.003 | 14/30 (HT-29, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.610×** | -4.2 | 0.003 | 11/46 (A498, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.559×** | -3.6 | 0.024 | 12/40 (SW1417, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.655×** | -3.6 | 0.024 | 10/45 (HT-29, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.565×** | -3.5 | 0.026 | 11/38 (A-427, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Malotilate (drug)]] 0.5 µM |  | **0.756×** | -3.3 | 0.050 | 11/43 (Panc 03.27, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 3.72 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +9.3) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0634× (z -9.9) |
| [[HCT15 (line)]] | alt | 4.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.49× (z +8.7) | — |
| [[LoVo (line)]] | wt | 3.03 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0667× (z -8.6) |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.105× (z -9.1) |
| [[A-172 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATE1OSP]] | +0.69 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[LINC02951]] | +0.66 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[C8orf44-SGK3]] | +0.66 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[YIPF4]] | +0.65 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[WDR45]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ZNF529-AS1]] | +0.62 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ZNF236-DT]] | +0.60 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[ING4]] | +0.60 | +0.27 / +0.70 | both halves | 3e-04 |  |
| [[BICRAL]] | +0.60 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[PPP1R12A-AS2]] | +0.59 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[ACTG1P17]] | +0.59 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[ACYP2]] | +0.59 | +0.67 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MC3]] ⚠ | -0.53 | -0.50 / -0.38 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[THEM6]] | -0.52 | -0.39 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NPIPB2's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-5.9, 24.2); signed map (30.5, -4.7). **Vector** length 54.7, 7.04% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +13.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.5 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +4.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.5 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -9.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -5.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.8 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | nuclear pore complex interacting protein family member B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:11,927,259-11,976,643 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A6NJ64](https://www.uniprot.org/uniprotkb/A6NJ64) carries no function annotation.

**Summary**, from NCBI Gene [729978](https://www.ncbi.nlm.nih.gov/gene/729978):

> Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:37451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37451) · Entrez [729978](https://www.ncbi.nlm.nih.gov/gene/729978) · UniProt [A6NJ64](https://www.uniprot.org/uniprotkb/A6NJ64) · Ensembl [ENSG00000234719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234719)

## Data

Gene col 13978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13978); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13978]; `tensor/DDL_lfc|DDL_z.npy` [13978]; `embed/gene_vectors.npy` [13978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13978 or target_col == 13978). Every well: [[NPIPB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPIPB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
