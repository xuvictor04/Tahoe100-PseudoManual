---
symbol: "TIGD2"
type: "gene"
col: 11099
ensembl_id: "ENSG00000180346"
name: "tigger transposable element derived 2"
location: "4q22.1"
module: 16
arm: "+"
pooled_cpm: 3.36
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# TIGD2

*tigger transposable element derived 2* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.32× (z +9.9, q 4e-20, up in 24 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.813× (z -5.9, q 2e-06, down in 31 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.553× (z -4.9, q 3e-04, down in 17 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VEZF1]] (+0.69, fdr 7e-06), [[RTL6]] (+0.68, fdr 7e-06), [[CSTF2T]] (+0.68, fdr 7e-06); moves opposite to [[SDHAP4-1]] (-0.65, fdr 7e-06), [[GNRH1]] (-0.65, fdr 1e-05), [[SGSM3]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.32×** | +9.9 | 4e-20 | 24/37 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.70×** | +8.2 | 6e-14 | 33/44 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.54×** | +7.7 | 2e-12 | 28/44 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.52×** | +7.4 | 2e-11 | 31/43 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +7.1 | 2e-10 | 31/44 (SW1417, HOP62, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +6.9 | 7e-10 | 28/45 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.18×** | +6.5 | 7e-09 | 21/33 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.93×** | +5.5 | 3e-06 | 20/41 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +5.3 | 6e-06 | 23/45 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +5.3 | 8e-06 | 18/45 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +4.1 | 0.002 | 13/40 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.004 | 7/44 (LoVo, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +3.7 | 0.010 | 11/45 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.55×** | +3.7 | 0.010 | 3/18 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.37×** | +3.6 | 0.012 | 7/44 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +3.4 | 0.019 | 7/39 (NCI-H460, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11099.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.813×** | -5.9 | 2e-06 | 31/47 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.553×** | -4.9 | 3e-04 | 17/43 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.587×** | -4.4 | 0.002 | 18/43 (RKO, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.619×** | -3.7 | 0.025 | 19/38 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | 0.492× | -3.1 | 0.24 | 6/30 (LOX-IMVI, LoVo, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 2.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 2.94 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0683× (z -11.0) |
| [[A-427 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.963 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[RTL6]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.68 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[RHOU]] | +0.66 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.65 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[PABIR1]] | +0.65 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[BBS10]] | +0.64 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[STX17]] | +0.64 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[C7orf25]] | +0.64 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[BIRC3]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ZBTB33]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP4-1]] | -0.65 | -0.71 / -0.58 | both halves | 7e-06 |  |
| [[GNRH1]] | -0.65 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[SGSM3]] | -0.64 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[RNF139-DT]] | -0.64 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[SMG1P5]] | -0.63 | -0.68 / -0.57 | both halves | 9e-06 |  |
| [[RARS2]] | -0.63 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[ASB16-AS1]] | -0.63 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ZCCHC17]] | -0.63 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[DIP2A]] | -0.63 | -0.77 / -0.56 | both halves | 1e-05 |  |
| [[GET1-SH3BGR]] | -0.63 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CD81]] | -0.62 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[ZFC3H1]] | -0.62 | -0.70 / -0.63 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises TIGD2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CAVIN2]] | B | CAVIN2 activity lowers TIGD2's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 1.23× higher at baseline in the lines without CAVIN2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9 |
| [[PUDP]] | C | PUDP activity raises TIGD2's level | lines that do not express PUDP (4) vs lines expressing it (46) | 1.35× lower at baseline in the lines without PUDP | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF264, ENSG00000287188 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.9, 12.4); signed map (1.5, -29.7). **Vector** length 61.8, 9.58% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +7.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.8 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | tigger transposable element derived 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:89,111,533-89,114,901 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Helix-turn-helix CENPB type domain family |
| Matched by | ensembl_id |

UniProt [Q4W5G0](https://www.uniprot.org/uniprotkb/Q4W5G0) carries no function annotation.

**Summary**, from NCBI Gene [166815](https://www.ncbi.nlm.nih.gov/gene/166815):

> The protein encoded by this gene belongs to the tigger subfamily of the pogo superfamily of DNA-mediated transposons in humans. These proteins are related to DNA transposons found in fungi and nematodes, and more distantly to the Tc1 and mariner transposases. They are also very similar to the major mammalian centromere protein B. The exact function of this gene is not known. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18333](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18333) · Entrez [166815](https://www.ncbi.nlm.nih.gov/gene/166815) · UniProt [Q4W5G0](https://www.uniprot.org/uniprotkb/Q4W5G0) · Ensembl [ENSG00000180346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180346)

## Data

Gene col 11099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11099); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11099]; `tensor/DDL_lfc|DDL_z.npy` [11099]; `embed/gene_vectors.npy` [11099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11099 or target_col == 11099). Every well: [[TIGD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIGD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
