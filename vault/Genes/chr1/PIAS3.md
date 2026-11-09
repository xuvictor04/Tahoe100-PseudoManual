---
symbol: "PIAS3"
type: "gene"
col: 5247
ensembl_id: "ENSG00000131788"
name: "protein inhibitor of activated STAT 3"
location: "1q21.1"
module: 2
arm: "+"
pooled_cpm: 20.88
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PIAS3

*protein inhibitor of activated STAT 3* — 1q21.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.434× (z -7.1, q 8e-10, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIX1L]] (+0.56, fdr 1e-05), [[SS18]] (+0.51, fdr 2e-05), [[PYGO2]] (+0.50, fdr 3e-05); moves opposite to [[LINC00536]] (-0.47, fdr 4e-05), [[NSMCE2]] (-0.42, fdr 6e-05), [[ARL17A]] (-0.42, fdr 2e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00536]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.23× | +3.3 | 0.42 | 13/44 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.2 | 0.42 | 1/48 (NCI-H23) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5247.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.434×** | -7.1 | 8e-10 | 34/48 (Panc 03.27, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.679×** | -6.3 | 8e-08 | 29/47 (SW480, NCI-H23, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.502×** | -5.8 | 9e-07 | 29/45 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.731×** | -4.8 | 2e-04 | 26/48 (AsPC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.751×** | -4.7 | 4e-04 | 20/47 (hTERT-HPNE, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.765×** | -4.4 | 0.001 | 23/47 (HS-578T, A-172, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.601×** | -4.3 | 0.001 | 11/28 (PANC-1, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.779×** | -4.1 | 0.003 | 19/48 (A498, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.786×** | -3.9 | 0.005 | 19/47 (HS-578T, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[NG25 (drug)]] 5 µM |  | **0.635×** | -3.9 | 0.006 | 16/45 (HepG2/C3A, Hs 766T, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.796×** | -3.7 | 0.010 | 20/46 (KATO III, SNU-1, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.858× | -3.6 | 0.018 | 15/47 (SNU-1, Hs 766T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.814×** | -3.4 | 0.033 | 19/48 (HS-578T, NCI-H661, …) | rises with dose |  |
| [[Cilostazol (drug)]] 5 µM |  | **0.811×** | -3.3 | 0.037 | 6/47 (NCI-H2347, PANC-1, …) | top dose only | position effect removed |
| [[Allantoin (drug)]] 0.5 µM |  | **0.818×** | -3.3 | 0.037 | 12/48 (HCT15, RKO, …) | inconsistent across doses | position effect removed |
| [[Adenosine (drug)]] 5 µM |  | 0.873× | -3.1 | 0.057 | 11/48 (A549, NCI-H2347, …) | top dose only | position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | **0.824×** | -3.0 | 0.070 | 13/47 (AsPC-1, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.818×** | -3.0 | 0.070 | 11/46 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 9.71 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 55.9 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[AsPC-1 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HS-578T (line)]] | alt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.278× (z -8.5) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.329× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[NCI-H23 (line)]] | alt | 40.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0613× (z -9.9) |
| [[PANC-1 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.213× (z -8.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIX1L]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[SS18]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PYGO2]] | +0.50 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ULK3]] | +0.48 | +0.43 / +0.37 | both halves | 8e-05 | same gene group |
| [[EMD]] | +0.47 | +0.45 / +0.43 | both halves | 4e-05 |  |
| [[SLC25A22]] | +0.47 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[BBS2]] | +0.47 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[SHC1]] | +0.46 | +0.40 / +0.44 | both halves | 4e-05 |  |
| [[LZTR1]] | +0.46 | +0.46 / +0.39 | both halves | 6e-05 |  |
| [[TMEM214]] | +0.45 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[FKBP5]] | +0.45 | +0.38 / +0.46 | both halves | 7e-05 | same gene group |
| [[TFCP2L1]] | +0.45 | +0.46 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00536]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[NSMCE2]] | -0.42 | -0.38 / -0.39 | both halves | 6e-05 | same gene group; pathway: SUMO E3 ligases SUMOylate target proteins; STRING 705 |
| [[ARL17A]] | -0.42 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[CHMP1B-AS1]] | -0.42 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[NPIPB12]] | -0.41 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[AGAP4]] | -0.41 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[IGBP1]] | -0.40 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[ENKUR]] | -0.39 | -0.42 / -0.32 | both halves | 1e-04 |  |
| [[TMEM116]] | -0.39 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[NSA2]] | -0.39 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[TBC1D22A]] | -0.39 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[VTI1A]] | -0.38 | -0.32 / -0.38 | both halves | 2e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00536]] | B | LINC00536 activity raises PIAS3's level | lines that do not express LINC00536 (17) vs lines expressing it (33) | 1.26× lower at baseline in the lines without LINC00536 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, DOCK2, LDOC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.306). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-20.8, -50.4); signed map (-25.2, -1.8). **Vector** length 70.6, 11.3% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.9 | +2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.6 | +3.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +0.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.3 | -7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -2.8 | -2.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.7 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | protein inhibitor of activated STAT 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:145,848,522-145,859,836 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14651, ZMIZ5 |
| Gene groups (HGNC) | Zinc fingers MIZ-type; MicroRNA protein coding host genes |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 11 pathways, smallest: SUMOylation of immune response proteins; SUMOylation of transcription factors; SUMOylation of intracellular receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6X2](https://www.uniprot.org/uniprotkb/Q9Y6X2) (E3 SUMO-protein ligase PIAS3):

> Functions as an E3-type small ubiquitin-like modifier (SUMO) ligase, stabilizing the interaction between UBE2I and the substrate, and as a SUMO-tethering factor. Plays a crucial role as a transcriptional coregulation in various cellular pathways, including the STAT pathway and the steroid hormone signaling pathway. Involved in regulating STAT3 signaling via inhibiting STAT3 DNA-binding and suppressing cell growth. Enhances the sumoylation of MTA1 and may participate in its paralog-selective …

**Summary**, from NCBI Gene [10401](https://www.ncbi.nlm.nih.gov/gene/10401):

> This gene encodes a member of the PIAS [protein inhibitor of activated STAT (signal transducer and activator of transcription)] family of transcriptional modulators. The protein functions as a SUMO (small ubiquitin-like modifier)-E3 ligase which catalyzes the covalent attachment of a SUMO protein to specific target substrates. It directly binds to several transcription factors and either blocks or enhances their activity. Alternatively spliced transcript variants of this gene have been …

**Accessions** — [HGNC:16861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16861) · Entrez [10401](https://www.ncbi.nlm.nih.gov/gene/10401) · UniProt [Q9Y6X2](https://www.uniprot.org/uniprotkb/Q9Y6X2) · Ensembl [ENSG00000131788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131788)

## Data

Gene col 5247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5247); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5247]; `tensor/DDL_lfc|DDL_z.npy` [5247]; `embed/gene_vectors.npy` [5247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5247 or target_col == 5247). Every well: [[PIAS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIAS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
