---
symbol: "SRM"
type: "gene"
col: 3812
ensembl_id: "ENSG00000116649"
name: "spermidine synthase"
location: "1p36.22"
module: 36
arm: "+"
pooled_cpm: 16.99
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SRM

*spermidine synthase* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.42× (z +10.0, q 1e-20, up in 33 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 2.31× (z +3.5, q 0.029, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.598× (z -5.9, q 2e-06, down in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.188×, HS-578T 0.282×, HOP62 0.259×, RPMI-7951 0.216×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (RKO 0.180×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.413×; ⚠ cell-cycle shift, explains ~84% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B4GALT2]] (+0.76, fdr 7e-06), [[TRIM27]] (+0.72, fdr 7e-06), [[WDR3]] (+0.72, fdr 7e-06); moves opposite to [[SNX16]] (-0.57, fdr 6e-05), [[SDCBP]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSEN2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.42×** | +10.0 | 1e-20 | 33/40 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.07×** | +8.7 | 7e-16 | 23/28 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +6.6 | 6e-09 | 34/42 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.25×** | +6.1 | 2e-07 | 27/35 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.82×** | +4.6 | 4e-04 | 26/43 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +4.1 | 0.004 | 29/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.31×** | +3.5 | 0.029 | 26/46 (Hs 766T, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.55×** | +3.5 | 0.029 | 21/45 (PANC-1, NCI-H460, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.87×** | +3.2 | 0.084 | 16/46 (MIA PaCa-2, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.084 | 20/46 (A498, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.084 | 24/47 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 2.06× | +3.1 | 0.10 | 14/46 (CFPAC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | 2.04× | +3.0 | 0.10 | 17/45 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.45× | +3.0 | 0.10 | 18/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3812.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.188×, HS-578T 0.282×, HOP62 0.259×, RPMI-7951 0.216×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (RKO 0.180×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.413×; ⚠ cell-cycle shift, explains ~84% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.598×** | -5.9 | 2e-06 | 31/47 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.722×** | -3.8 | 0.050 | 23/48 (A498, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.685× | -3.1 | 0.39 | 21/46 (hTERT-HPNE, SW 1088, …) | rises with dose | cell-cycle shift (explains ~23% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 18.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.0) |
| [[RKO (line)]] | wt | 25.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.2) |
| [[A498 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.413× (z -8.6) ⚠ cell-cycle shift, explains ~84% of this change |
| [[Hs 766T (line)]] | wt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HS-578T (line)]] | alt | 37.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2030 (line)]] | alt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.31× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -10.1) |
| [[SNU-423 (line)]] | alt | 8.30 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.63× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALT2]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[TRIM27]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[WDR3]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.71 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[XPO4]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[URB2]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[URB1]] | +0.67 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[RABEPK]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[VKORC1L1]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX16]] | -0.57 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[SDCBP]] | -0.55 | -0.43 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSEN2]] | C | TSEN2 activity raises SRM's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 1.90× lower at baseline in the lines without TSEN2 | 0.082 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-5.3, -28.7); signed map (-45.2, -18.1). **Vector** length 78.8, 20.2% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +2.9 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -4.1 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -0.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | spermidine synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,054,584-11,060,020 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPS1; previously SRML1 |
| Gene groups (HGNC) | 7BS non-methyltransferases |
| Hallmark sets | MYC_TARGETS_V2, MYC_TARGETS_V1 |
| Reactome | 2 pathways, smallest: Metabolism of polyamines; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P19623](https://www.uniprot.org/uniprotkb/P19623) (Spermidine synthase):

> Catalyzes the production of spermidine from putrescine and decarboxylated S-adenosylmethionine (dcSAM). Has a strong preference for putrescine as substrate, and has very low activity towards 1,3-diaminopropane. Has extremely low activity towards spermidine.

**Summary**, from NCBI Gene [6723](https://www.ncbi.nlm.nih.gov/gene/6723):

> The polyamines putrescine, spermine, and spermidine are ubiquitous polycationic mediators of cell growth and differentiation. Spermidine synthase is one of four enzymes in the polyamine-biosynthetic pathway and carries out the final step of spermidine biosynthesis. This enzyme catalyzes the conversion of putrescine to spermidine using decarboxylated S-adenosylmethionine as the cofactor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11296) · Entrez [6723](https://www.ncbi.nlm.nih.gov/gene/6723) · UniProt [P19623](https://www.uniprot.org/uniprotkb/P19623) · Ensembl [ENSG00000116649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116649)

## Data

Gene col 3812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3812); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3812]; `tensor/DDL_lfc|DDL_z.npy` [3812]; `embed/gene_vectors.npy` [3812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3812 or target_col == 3812). Every well: [[SRM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
