---
symbol: "ANAPC15"
type: "gene"
col: 3122
ensembl_id: "ENSG00000110200"
name: "anaphase promoting complex subunit 15"
location: "11q13.4"
module: 29
arm: "+"
pooled_cpm: 7.49
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ANAPC15

*anaphase promoting complex subunit 15* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.18× (z +15.4, q 0e+00, up in 30 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +3.9, q 0.009, up in 17 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.409× (z -4.0, q 0.038, down in 21 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0871×; ⚠ toxic); [[Rutin (trihydrate) (drug)]] 5 µM in 1 line (SW 900 0.0567×); [[Pemetrexed (drug)]] 5 µM in 1 line (HOP62 0.0781×); [[Paclitaxel (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0699×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGN2P5]] (+0.61, fdr 1e-05), [[CDKN2AIPNL]] (+0.55, fdr 1e-05), [[MYL9]] (+0.53, fdr 3e-05); moves opposite to [[THSD1]] (-0.42, fdr 2e-04), [[ACAP2]] (-0.40, fdr 4e-04), [[C9orf72]] (-0.40, fdr 1e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[UCP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.18×** | +15.4 | 0e+00 | 30/30 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.76×** | +14.3 | 1e-43 | 12/13 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.19×** | +9.8 | 2e-20 | 20/20 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **2.02×** | +5.9 | 4e-07 | 24/35 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.88×** | +5.3 | 1e-05 | 22/43 (KATO III, NCI-H460, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.63×** | +3.9 | 0.008 | 12/36 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.009 | 17/41 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[vincristine (drug)]] 5 µM |  | **2.09×** | +3.3 | 0.077 | 7/30 (A549, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.82×** | +3.2 | 0.077 | 17/43 (KATO III, HEC-1-A, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3122.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0871×; ⚠ toxic); [[Rutin (trihydrate) (drug)]] 5 µM in 1 line (SW 900 0.0567×); [[Pemetrexed (drug)]] 5 µM in 1 line (HOP62 0.0781×); [[Paclitaxel (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0699×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.409×** | -4.0 | 0.038 | 21/46 (HCT15, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.674× | -3.4 | 0.20 | 16/46 (J82, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.80 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.85× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 8.63 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.45× (z +9.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 11.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.18× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 10.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.45× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 7.32 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.99× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 7.22 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.43× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 7.97 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.18× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 3.73 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0781× (z -8.8) |
| [[KATO III (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.2× (z +12.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 5.14 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.9× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 6.62 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +8.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 4.48 | 0 | 1 | — | [[Paclitaxel (drug)]] 0.05 µM 0.0699× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 9.37 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0871× (z -10.5) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 7.46 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.6× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 4.57 | 0 | 1 | — | [[Rutin (trihydrate) (drug)]] 5 µM 0.0567× (z -8.8) |
| [[A-427 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN2P5]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[CDKN2AIPNL]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[MYL9]] | +0.53 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[NME4]] | +0.52 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[COMMD4]] | +0.49 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[HINT2]] | +0.49 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[MRPL11]] | +0.48 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[SPA17]] | +0.48 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[HNRNPK-AS1]] | +0.47 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[HYI]] | +0.46 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[TMEM19]] | +0.46 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[SUMO3]] | +0.46 | +0.45 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THSD1]] | -0.42 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[ACAP2]] | -0.40 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[C9orf72]] | -0.40 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[GAN]] | -0.40 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[SELENOS]] | -0.40 | -0.41 / -0.21 | both halves | 7e-04 |  |
| [[RBCK1]] | -0.39 | -0.39 / -0.24 | both halves | 5e-04 |  |
| [[SPIRE1]] | -0.38 | -0.46 / -0.21 | both halves | 7e-04 |  |
| [[FOXO3B]] | -0.38 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[SARS1]] | -0.37 | -0.37 / -0.26 | both halves | 3e-04 |  |
| [[TRAPPC12]] | -0.37 | -0.35 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UCP2]] | B | UCP2 activity raises ANAPC15's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.33× lower at baseline in the lines without UCP2 | 0.074 | ⚠ within organs, on part of the lines; also absent: WNK2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.321). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-46.8, -37.1); signed map (34.9, -29.0). **Vector** length 43.2, 5.80% of its response variance represented; |z| ≥ 3 in 606 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +14.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | -0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | -0.3 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | anaphase promoting complex subunit 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:72,106,378-72,112,780 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC020, DKFZP564M082, APC15; previously C11orf51 |
| Gene groups (HGNC) | Anaphase promoting complex |
| Reactome | 39 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [P60006](https://www.uniprot.org/uniprotkb/P60006) (Anaphase-promoting complex subunit 15):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. APC/C catalyzes assembly of branched 'Lys-11'-/'Lys-48'-linked branched ubiquitin chains on …

**Summary**, from NCBI Gene [25906](https://www.ncbi.nlm.nih.gov/gene/25906):

> Involved in anaphase-promoting complex-dependent catabolic process; protein polyubiquitination; and regulation of mitotic cell cycle spindle assembly checkpoint. Part of anaphase-promoting complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24531) · Entrez [25906](https://www.ncbi.nlm.nih.gov/gene/25906) · UniProt [P60006](https://www.uniprot.org/uniprotkb/P60006) · Ensembl [ENSG00000110200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110200)

## Data

Gene col 3122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3122); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3122]; `tensor/DDL_lfc|DDL_z.npy` [3122]; `embed/gene_vectors.npy` [3122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3122 or target_col == 3122). Every well: [[ANAPC15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
