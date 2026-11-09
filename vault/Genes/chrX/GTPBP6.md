---
symbol: "GTPBP6"
type: "gene"
col: 10941
ensembl_id: "ENSG00000178605"
name: "GTP binding protein 6"
location: "Xp22.33 and Yp11.32"
module: 18
arm: "+"
pooled_cpm: 12.36
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# GTPBP6

*GTP binding protein 6* — Xp22.33 and Yp11.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.66× (z +15.0, q 0e+00, up in 35 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.48× (z +6.1, q 2e-07, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.608× (z -7.6, q 1e-11, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTA1]] (+0.67, fdr 9e-06), [[DAZAP1]] (+0.64, fdr 1e-05), [[CPNE7]] (+0.60, fdr 1e-05); moves opposite to [[SNRPB2]] (-0.47, fdr 7e-05), [[HPF1]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +15.0 | 0e+00 | 35/38 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +12.7 | 1e-34 | 19/23 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +10.2 | 3e-22 | 23/28 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +6.1 | 2e-07 | 20/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +4.9 | 1e-04 | 18/46 (NCI-H2030, COLO 205, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.4 | 0.001 | 12/46 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.1 | 0.004 | 12/47 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.004 | 9/43 (A-172, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.9 | 0.005 | 14/40 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.9 | 0.005 | 15/41 (LoVo, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.9 | 0.005 | 15/42 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +3.5 | 0.022 | 15/46 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.027 | 7/42 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.4 | 0.027 | 7/26 (SW480, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.080 | 8/39 (PANC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10941.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.608×** | -7.6 | 1e-11 | 26/47 (SNU-423, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.633×** | -7.0 | 7e-10 | 28/47 (NCI-H1792, BT-474, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.650×** | -6.6 | 8e-09 | 24/47 (SW1417, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.667×** | -6.2 | 8e-08 | 20/47 (AN3 CA, KATO III, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -4.4 | 0.002 | 7/48 (SNU-423, SHP-77, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.757×** | -4.3 | 0.002 | 13/45 (HepG2/C3A, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.613×** | -3.9 | 0.007 | 12/47 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.777×** | -3.9 | 0.008 | 14/46 (C-33 A, SNU-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.780×** | -3.7 | 0.016 | 10/45 (PANC-1, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 4.36 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0824× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -8.6) ⚠ toxic |
| [[H4 (line)]] | wt | 16.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.143× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 15.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 8.93 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0918× (z -8.9) |
| [[J82 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.230× (z -13.9) ⚠ cell-cycle shift, explains ~6% of this change |
| [[LoVo (line)]] | wt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 9.46 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.31× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTA1]] | +0.67 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[DAZAP1]] | +0.64 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CPNE7]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[DPP7]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[OPLAH]] ⚠ | +0.58 | +0.57 / +0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[WDR6]] | +0.58 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[DUS3L]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[MTSS2]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[PRMT1]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[MRPS25]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[CLUH]] | +0.53 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[GIGYF1]] | +0.53 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[WIZ]] | +0.53 | +0.40 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB2]] | -0.47 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[HPF1]] | -0.44 | -0.38 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises GTPBP6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.407). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-13.0, -27.6); signed map (-2.0, -55.5). **Vector** length 64.1, 9.92% of its response variance represented; |z| ≥ 3 in 764 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +10.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | GTP binding protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 and Yp11.32 — chrX:304,529-318,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PGPL, FLJ20977 |
| Gene groups (HGNC) | Pseudoautosomal region 1 |
| Matched by | ensembl_id |

**Function**, from UniProt [O43824](https://www.uniprot.org/uniprotkb/O43824) (GTP-binding protein 6):

> Mitochondrial GTP-binding protein involved in mitochondrial ribosome biogenesis and ribosome recycling. Promotes late-stage maturation of the peptidyl transferase center during mitochondrial large ribosomal subunit (mt-LSU) biogenesis by inducing conformational rearrangements that drive its progression to a near-mature state. Acts as a ribosome recycling factor that promotes dissociation of mature mitochondrial ribosomes into the small (mt-SSU) and large (mt-LSU) ribosomal subunits.

**Summary**, from NCBI Gene [8225](https://www.ncbi.nlm.nih.gov/gene/8225):

> This gene encodes a GTP binding protein and is located in the pseudoautosomal region (PAR) at the end of the short arms of the X and Y chromosomes. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:30189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30189) · Entrez [8225](https://www.ncbi.nlm.nih.gov/gene/8225) · UniProt [O43824](https://www.uniprot.org/uniprotkb/O43824) · Ensembl [ENSG00000178605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178605)

## Data

Gene col 10941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10941); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10941]; `tensor/DDL_lfc|DDL_z.npy` [10941]; `embed/gene_vectors.npy` [10941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10941 or target_col == 10941). Every well: [[GTPBP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTPBP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
