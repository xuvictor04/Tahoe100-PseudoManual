---
symbol: "NDUFA4"
type: "gene"
col: 12078
ensembl_id: "ENSG00000189043"
name: "cytochrome c oxidase associated subunit FA4"
location: "7p21.3"
module: 48
arm: "+"
pooled_cpm: 91.39
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# NDUFA4

*cytochrome c oxidase associated subunit FA4* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.41× (z +9.1, q 7e-17, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.92× (z +4.0, q 0.007, up in 39 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.155×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX6C]] (+0.86, fdr 7e-06), [[COX6B1]] (+0.83, fdr 7e-06), [[COX7C]] (+0.82, fdr 7e-06); moves opposite to [[TEX261]] (-0.70, fdr 1e-05), [[PSMG1]] (-0.66, fdr 1e-05), [[ZNF460]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12078.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **4.41×** | +9.1 | 7e-17 | 49/49 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **3.13×** | +6.7 | 5e-09 | 42/44 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.46×** | +5.5 | 7e-06 | 48/48 (NCI-H1573, SNU-1, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +5.1 | 5e-05 | 46/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.31×** | +4.7 | 3e-04 | 41/45 (A549, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.92×** | +4.0 | 0.007 | 39/48 (HOP62, COLO 205, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.84×** | +3.7 | 0.014 | 37/48 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.016 | 36/49 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +3.3 | 0.062 | 33/48 (HOP62, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +3.2 | 0.089 | 30/48 (HOP62, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.70×** | +3.1 | 0.094 | 44/48 (SW 1271, KATO III, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12078.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.155×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.344× | -3.4 | 0.38 | 44/49 (BT-474, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 84.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 90.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A498 (line)]] | wt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A549 (line)]] | wt | 61.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.13× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[AN3 CA (line)]] | alt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -9.5) |
| [[C32 (line)]] | wt | 64.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HOP62 (line)]] | alt | 60.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.33× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HS-578T (line)]] | alt | 88.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.99× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 59.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[KATO III (line)]] | alt | 179 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[LoVo (line)]] | wt | 138 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[LOX-IMVI (line)]] | wt | 65.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 52.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H1573 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.50× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H460 (line)]] | wt | 90.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[PANC-1 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 77.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-427 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 19 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6C]] | +0.86 | +0.79 / +0.90 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[COX6B1]] | +0.83 | +0.74 / +0.86 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[COX7C]] | +0.82 | +0.75 / +0.86 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[NDUFA1]] | +0.82 | +0.75 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 995 |
| [[UQCRQ]] ⚠ | +0.81 | +0.71 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 980; ⚠ in the vector space only through flagged drug-doses |
| [[UBL5]] | +0.80 | +0.74 / +0.83 | both halves | 7e-06 |  |
| [[COX7A2]] ⚠ | +0.80 | +0.67 / +0.85 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 997; ⚠ in the vector space only through flagged drug-doses |
| [[UQCRB]] ⚠ | +0.79 | +0.70 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 941; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB11]] ⚠ | +0.78 | +0.75 / +0.74 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 987; ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.77 | +0.71 / +0.80 | both halves | 7e-06 | STRING 717 |
| [[ATP5PD]] | +0.77 | +0.60 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 879 |
| [[ATP5F1E]] | +0.77 | +0.68 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 662 |
| [[COX6A1]] | +0.76 | +0.70 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998 |
| [[ATP5MK]] | +0.76 | +0.66 / +0.79 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 810 |
| [[NENF]] | +0.75 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[RPS19]] | +0.75 | +0.65 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX261]] | -0.70 | -0.50 / -0.70 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.66 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[ZNF460]] | -0.64 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[HGH1]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.840). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.5, -22.6); signed map (-35.2, 9.5). **Vector** length 72.5, 36.8% of its response variance represented; |z| ≥ 3 in 646 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.70 to 7); *Complex I biogenesis* (reactome, mean cos +0.64 to 9); *Cristae formation* (reactome, mean cos +0.70 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +3.5 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | -0.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -6.2 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -6.2 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -5.9 | +9.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase associated subunit FA4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:10,931,943-10,940,153 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MLRQ, CI-9k, MRCAF1, MISTR1; previously NDUFA4 |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O00483](https://www.uniprot.org/uniprotkb/O00483) (Cytochrome c oxidase subunit FA4):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [4697](https://www.ncbi.nlm.nih.gov/gene/4697):

> The protein encoded by this gene belongs to the complex I 9kDa subunit family. Mammalian complex I of mitochondrial respiratory chain is composed of 45 different subunits. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7687) · Entrez [4697](https://www.ncbi.nlm.nih.gov/gene/4697) · UniProt [O00483](https://www.uniprot.org/uniprotkb/O00483) · Ensembl [ENSG00000189043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189043)

## Data

Gene col 12078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12078); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12078]; `tensor/DDL_lfc|DDL_z.npy` [12078]; `embed/gene_vectors.npy` [12078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12078 or target_col == 12078). Every well: [[NDUFA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
