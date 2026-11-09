---
symbol: "C9orf64"
type: "gene"
col: 9071
ensembl_id: "ENSG00000165118"
name: "Q-nucleotide N-glycosylase 1"
location: "9q21.32"
module: 16
arm: "+"
pooled_cpm: 9.38
n_lines_expressing: 44
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# C9orf64

*Q-nucleotide N-glycosylase 1* — 9q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.67× (z +6.0, q 8e-07, up in 8 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.41× (z +5.9, q 8e-07, up in 19 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.456× (z -9.6, q 3e-19, down in 29 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.531× (z -7.8, q 2e-12, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C7orf25]] (+0.73, fdr 7e-06), [[TASOR]] (+0.71, fdr 1e-05), [[CENPBD1P]] (+0.70, fdr 9e-06); moves opposite to [[CBFA2T2]] (-0.69, fdr 1e-05), [[RPLP2]] (-0.66, fdr 2e-05), [[RPS21]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LLGL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9071.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.0 | 8e-07 | 8/16 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +5.9 | 8e-07 | 19/40 (SK-MEL-2, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.3 | 2e-05 | 17/42 (SW480, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.44×** | +4.4 | 0.002 | 13/29 (KATO III, SW1417, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.002 | 20/41 (C-33 A, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.004 | 16/38 (NCI-H23, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.0 | 0.004 | 11/31 (PANC-1, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.005 | 11/39 (COLO 205, NCI-H2347, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.012 | 11/39 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.023 | 12/40 (SNU-423, LoVo, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.036 | 8/39 (A-427, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.037 | 6/41 (NCI-H1792, SW480, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.037 | 10/41 (C-33 A, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.037 | 14/40 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.21×** | +3.3 | 0.043 | 9/42 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[OTS514 (drug)]] 5 µM |  | **1.61×** | +3.0 | 0.087 | 4/31 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9071.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.456×** | -9.6 | 3e-19 | 29/39 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.531×** | -7.8 | 2e-12 | 26/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.571×** | -6.9 | 1e-09 | 26/40 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.625×** | -5.8 | 1e-06 | 24/41 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.683×** | -4.7 | 3e-04 | 17/41 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.725×** | -4.0 | 0.006 | 15/41 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.712×** | -4.0 | 0.006 | 16/39 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.757×** | -3.5 | 0.039 | 13/41 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.762×** | -3.4 | 0.049 | 16/41 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.55 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0740× (z -15.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -11.1) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.175× (z -9.3) |
| [[SW480 (line)]] | alt | 13.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.286× (z -9.4) |
| [[A-427 (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.205× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~76% of this change |
| [[A549 (line)]] | wt | 9.43 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0490× (z -13.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 4.37 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0610× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.111× (z -9.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 5.19 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM 0.0837× (z -8.8) |
| [[J82 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -14.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 3.25 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0787× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.169× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~63% of this change |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -11.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.876 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C7orf25]] | +0.73 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[TASOR]] | +0.71 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[CENPBD1P]] | +0.70 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[DCLRE1A]] | +0.70 | +0.79 / +0.57 | both halves | 9e-06 |  |
| [[ZXDB]] | +0.68 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[GTF3C4]] | +0.67 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[ADO]] | +0.67 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[CYREN]] | +0.66 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[DDX20]] | +0.66 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[BBS10]] | +0.66 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[USP7]] | +0.65 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[ZNF543]] | +0.65 | +0.70 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.69 | -0.77 / -0.50 | both halves | 1e-05 |  |
| [[RPLP2]] | -0.66 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[RPS21]] | -0.64 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[RPS29]] | -0.60 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[RPS25]] | -0.60 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[COX6A1]] | -0.60 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[FAM118A]] | -0.59 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[PI4KAP2]] | -0.59 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[RPL28]] | -0.58 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[SNHG25]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[RPL38]] | -0.58 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[GABARAPL2]] | -0.58 | -0.53 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LLGL2]] | B | LLGL2 activity raises C9orf64's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.93× lower at baseline in the lines without LLGL2 | 0.057 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[HDAC6]] | B | HDAC6 activity raises C9orf64's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises C9orf64's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.3, 13.3); signed map (4.0, -34.6). **Vector** length 64.0, 10.9% of its response variance represented; |z| ≥ 3 in 756 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.2 | +5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -0.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -9.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -6.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.2 | -2.4 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | Q-nucleotide N-glycosylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.32 — chr9:83,938,311-83,956,986 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10999; previously C9orf64 |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T6V5](https://www.uniprot.org/uniprotkb/Q5T6V5) (Queuosine 5'-phosphate N-glycosylase/hydrolase):

> Catalyzes the hydrolysis of queuosine 5'-phosphate, releasing the nucleobase queuine (q). Is required for salvage of queuine from exogenous queuosine (Q) that is imported and then converted to queuosine 5'-phosphate intracellularly. In vitro, can also catalyze the release of the q base directly from Q as substrate; however, it was shown that Q is not the biologically relevant substrate. Shows a very low activity on queuosine 3',5'-diphosphate, and cannot release q from queuosine 3'-phosphate …

**Summary**, from NCBI Gene [84267](https://www.ncbi.nlm.nih.gov/gene/84267):

> Enables queuosine nucleosidase activity. Involved in nucleoside salvage. Is active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28144](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28144) · Entrez [84267](https://www.ncbi.nlm.nih.gov/gene/84267) · UniProt [Q5T6V5](https://www.uniprot.org/uniprotkb/Q5T6V5) · Ensembl [ENSG00000165118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165118)

## Data

Gene col 9071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9071); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9071]; `tensor/DDL_lfc|DDL_z.npy` [9071]; `embed/gene_vectors.npy` [9071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9071 or target_col == 9071). Every well: [[C9orf64 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C9orf64.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
