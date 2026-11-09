---
symbol: "UBE2Q1"
type: "gene"
col: 8373
ensembl_id: "ENSG00000160714"
name: "ubiquitin conjugating enzyme E2 Q1"
location: "1q21.3"
module: 7
arm: "+"
pooled_cpm: 39.49
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# UBE2Q1

*ubiquitin conjugating enzyme E2 Q1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.05× (z +10.6, q 9e-24, up in 40 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.36× (z +6.6, q 8e-09, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM: 0.792× (z -4.9, q 6e-04, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM184C]] (+0.60, fdr 1e-05), [[ACIN1]] (+0.60, fdr 1e-05), [[TCEAL1]] (+0.60, fdr 2e-05); moves opposite to [[GRK6]] (-0.52, fdr 4e-05), [[NPHP4]] (-0.51, fdr 1e-04), [[NHP2]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8373.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +10.6 | 9e-24 | 40/45 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +10.6 | 9e-24 | 36/41 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.7 | 3e-09 | 36/46 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +6.6 | 8e-09 | 38/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +5.4 | 8e-06 | 32/49 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +5.3 | 1e-05 | 27/46 (SW1417, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +4.8 | 1e-04 | 26/43 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.24×** | +4.6 | 3e-04 | 25/48 (A-427, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.006 | 22/48 (A-427, AN3 CA, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.006 | 24/48 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **1.25×** | +3.3 | 0.058 | 21/47 (SHP-77, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.792×** | -4.9 | 6e-04 | 27/48 (SHP-77, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.761×** | -4.1 | 0.014 | 22/48 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.791×** | -3.5 | 0.067 | 21/48 (KATO III, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.847× | -3.5 | 0.067 | 17/48 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **0.792×** | -3.4 | 0.067 | 18/48 (SW480, A549, …) | inconsistent across doses | position effect removed |
| [[Isocorydine (drug)]] 5 µM |  | 0.862× | -3.1 | 0.18 | 10/48 (HT-29, A-427, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 53.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.2) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[A498 (line)]] | wt | 45.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +10.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 36.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 34.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 40.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 44.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.0) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[KATO III (line)]] | alt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 80.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 47.9 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.57× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 43.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.7) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[PANC-1 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 56.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM184C]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ACIN1]] | +0.60 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TCEAL1]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[DNAJA2]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[BROX]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[WASHC2C]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[WASHC2A]] | +0.57 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[RRAGB]] | +0.56 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ZNF616]] | +0.56 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ZNF428]] | +0.56 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[FUNDC1]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PBX2]] | +0.56 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRK6]] | -0.52 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[NPHP4]] | -0.51 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[NHP2]] | -0.51 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[CENPX]] | -0.50 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[POC1A]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PBX4]] | -0.48 | -0.51 / -0.25 | both halves | 4e-04 |  |
| [[SRPK1]] | -0.48 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[PSD3]] | -0.47 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[DGKD]] | -0.47 | -0.43 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises UBE2Q1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CLPX]] | C | CLPX's natural level weakens UBE2Q1's drug response | CLPX's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.22; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.416). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-20.3, 12.7); signed map (11.5, -27.3). **Vector** length 75.9, 16.3% of its response variance represented; |z| ≥ 3 in 660 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.9 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +5.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.6 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.3 | +3.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.0 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.3 | +1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.3 | -0.1 |
|  | [[vincristine (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 Q1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,548,577-154,559,028 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRO3094, NICE-5; previously UBE2Q |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7E8](https://www.uniprot.org/uniprotkb/Q7Z7E8) (Ubiquitin-conjugating enzyme E2 Q1):

> Catalyzes the covalent attachment of ubiquitin to other proteins. May be involved in hormonal homeostasis in females. Involved in regulation of B4GALT1 cell surface expression, B4GALT1-mediated cell adhesion to laminin and embryoid body formation (By similarity).

**Summary**, from NCBI Gene [55585](https://www.ncbi.nlm.nih.gov/gene/55585):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes (E1s), ubiquitin-conjugating enzymes (E2s), and ubiquitin-protein ligases (E3s). This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. The encoded protein is 98% identical to the mouse counterpart. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15698) · Entrez [55585](https://www.ncbi.nlm.nih.gov/gene/55585) · UniProt [Q7Z7E8](https://www.uniprot.org/uniprotkb/Q7Z7E8) · Ensembl [ENSG00000160714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160714)

## Data

Gene col 8373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8373); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8373]; `tensor/DDL_lfc|DDL_z.npy` [8373]; `embed/gene_vectors.npy` [8373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8373 or target_col == 8373). Every well: [[UBE2Q1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2Q1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
