---
symbol: "GTF2IP5"
type: "gene"
col: 13395
ensembl_id: "ENSG00000224316"
name: "general transcription factor IIi pseudogene 5"
location: "7q11.21"
module: 35
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# GTF2IP5

*general transcription factor IIi pseudogene 5* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.84× (z +16.4, q 0e+00, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.512× (z -7.5, q 3e-11, down in 19 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.521× (z -7.3, q 6e-11, down in 20 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2IP14]] (+0.77, fdr 7e-06), [[ACTG1P17]] (+0.71, fdr 7e-06), [[NSMCE1-DT]] (+0.70, fdr 7e-06); moves opposite to [[SPIDR]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +16.4 | 0e+00 | 24/28 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.79×** | +9.1 | 2e-17 | 26/45 (SW480, SW48, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +6.7 | 3e-09 | 9/30 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.2 | 1e-07 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.5 | 4e-06 | 7/22 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.4 | 8e-06 | 13/35 (SW48, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +5.0 | 4e-05 | 4/12 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +4.4 | 6e-04 | 3/39 (KATO III, SW48, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.4 | 8e-04 | 6/29 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.003 | 0/43 | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.003 | 9/45 (C32, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.004 | 3/47 (A498, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.006 | 4/44 (HEC-1-A, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +3.6 | 0.012 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.012 | 5/44 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.038 | 3/41 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.66×** | +2.9 | 0.100 | 0/21 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.512×** | -7.5 | 3e-11 | 19/46 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.521×** | -7.3 | 6e-11 | 20/41 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.545×** | -6.8 | 2e-09 | 15/36 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.589×** | -6.0 | 3e-07 | 11/19 (PANC-1, MIA PaCa-2, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -4.0 | 0.007 | 11/41 (HS-578T, CFPAC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -3.5 | 0.048 | 12/44 (A498, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.741×** | -3.3 | 0.087 | 13/19 (LoVo, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.756×** | -3.2 | 0.098 | 4/44 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.748×** | -3.2 | 0.098 | 8/36 (C32, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.760× | -3.1 | 0.10 | 8/46 (SW48, PANC-1, …) | all doses, stronger at high dose |  |
| [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | 0.765× | -3.0 | 0.12 | 6/43 (SHP-77, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 7.83 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -10.4) |
| [[A498 (line)]] | wt | 2.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 5.69 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0825× (z -10.2) |
| [[PANC-1 (line)]] | alt | 3.47 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 3.01 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.661 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.938 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.755 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.796 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IP14]] | +0.77 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[ACTG1P17]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[NSMCE1-DT]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[DDX59-AS1]] | +0.69 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PPP1R42]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[C11orf71]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TERB1]] | +0.66 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[LINC00663]] | +0.65 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[PSMD14-DT]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[RAD9B]] | +0.64 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[MALINC1]] | +0.64 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.63 | +0.64 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPIDR]] | -0.55 | -0.41 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GTF2IP5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (5.2, 21.6); signed map (31.8, -7.0). **Vector** length 41.8, 4.46% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.4 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +16.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +1.9 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.8 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.2 | -7.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | +1.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -0.9 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIi pseudogene 5 |
| Locus type | pseudogene |
| Location | 7q11.21 — chr7:65,773,620-65,802,067 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51717) · Entrez [100420546](https://www.ncbi.nlm.nih.gov/gene/100420546) · Ensembl [ENSG00000224316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224316)

## Data

Gene col 13395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13395); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13395]; `tensor/DDL_lfc|DDL_z.npy` [13395]; `embed/gene_vectors.npy` [13395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13395 or target_col == 13395). Every well: [[GTF2IP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2IP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
