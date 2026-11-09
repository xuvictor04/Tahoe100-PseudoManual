---
symbol: "POLR2M"
type: "gene"
col: 14945
ensembl_id: "ENSG00000255529"
name: "RNA polymerase II subunit M"
location: "15q21.3"
module: 135
arm: "+"
pooled_cpm: 11.06
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# POLR2M

*RNA polymerase II subunit M* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.12× (z +19.0, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.684× (z -6.8, q 7e-09, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZXDB]] (+0.78, fdr 7e-06), [[TRMO]] (+0.75, fdr 7e-06), [[RNF6]] (+0.74, fdr 2e-05); moves opposite to [[PCMT1]] (-0.66, fdr 9e-05), [[GNA12]] (-0.66, fdr 1e-04), [[METRN]] (-0.66, fdr 4e-05).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ANKEF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14945.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +19.0 | 0e+00 | 41/46 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +12.6 | 3e-34 | 34/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +11.3 | 4e-27 | 15/30 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +9.8 | 1e-20 | 32/43 (RKO, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +9.4 | 1e-18 | 33/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +8.7 | 4e-16 | 26/47 (A498, LoVo, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +7.7 | 2e-12 | 23/42 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +7.4 | 1e-11 | 22/47 (NCI-H2347, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.4 | 1e-08 | 21/44 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +5.6 | 1e-06 | 19/46 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.5 | 2e-06 | 8/20 (NCI-H2030, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +5.4 | 3e-06 | 15/47 (SW480, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 5e-06 | 15/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +5.1 | 2e-05 | 13/47 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +4.7 | 8e-05 | 13/46 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.66×** | +4.7 | 9e-05 | 9/47 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 9e-04 | 11/46 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.004 | 3/46 (LoVo, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.006 | 6/47 (SW480, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14945.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.684×** | -6.8 | 7e-09 | 21/47 (NCI-H1573, A-427, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.714×** | -6.0 | 5e-07 | 19/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.743×** | -5.3 | 2e-05 | 9/47 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.744×** | -5.3 | 2e-05 | 19/47 (KATO III, SW480, …) | all doses, flat | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.740×** | -5.2 | 3e-05 | 19/46 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.781×** | -4.4 | 0.001 | 12/46 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | **0.797×** | -3.7 | 0.015 | 10/46 (NCI-H2347, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.691×** | -3.4 | 0.041 | 5/48 (HCT15, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.833×** | -3.3 | 0.071 | 13/46 (SW48, A549, …) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | 0.885× | -3.1 | 0.12 | 14/46 (H4, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 14.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 12.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 10.5× (z +15.0) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.274× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.93× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 6.23 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0647× (z -8.5) |
| [[Hs 766T (line)]] | wt | 8.77 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM 0.141× (z -8.8) |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0990× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 9.15 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.220× (z -8.7) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0709× (z -14.2) |
| [[SW48 (line)]] | wt | 11.0 | 0 | 1 | — | [[Fumaric acid (drug)]] 0.05 µM 0.0706× (z -9.2) |
| [[A-172 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDB]] | +0.78 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[TRMO]] | +0.75 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[RNF6]] | +0.74 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[ZXDA]] | +0.74 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ZNF189]] | +0.71 | +0.71 / +0.39 | both halves | 5e-05 |  |
| [[KRBA2]] | +0.68 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[SNAPC5]] | +0.68 | +0.69 / +0.39 | both halves | 5e-05 |  |
| [[UBE2D3-AS1]] | +0.67 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[ZNF610]] | +0.67 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[EIF5]] | +0.67 | +0.64 / +0.30 | both halves | 2e-04 |  |
| [[PEF1]] | +0.67 | +0.65 / +0.33 | both halves | 1e-04 |  |
| [[BAG2]] | +0.66 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | -0.66 | -0.59 / -0.37 | both halves | 9e-05 |  |
| [[GNA12]] | -0.66 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[METRN]] | -0.66 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[DHTKD1]] | -0.65 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[SFI1]] | -0.63 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.63 | -0.65 / -0.33 | both halves | 1e-04 |  |
| [[TSEN54]] | -0.62 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[FAM118A]] | -0.62 | -0.71 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[GMCL1]] | -0.62 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[SH3GL1]] | -0.62 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PI4KA]] | -0.62 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[COX6A1]] | -0.61 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[KIAA1958]] | -0.61 | -0.57 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKEF1]] | B | ANKEF1 activity raises POLR2M's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without ANKEF1 | 0.078 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| [[HDAC6]] | B | HDAC6 activity raises POLR2M's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-17.8, 8.4); signed map (8.7, -29.3). **Vector** length 74.8, 12.4% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.1 | +12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +19.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +9.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +8.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.4 | -6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -6.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.5 | -5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | -5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -5.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II subunit M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:57,706,695-57,782,762 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Gdown, Gdown1; previously GRINL1A |
| Gene groups (HGNC) | RNA polymerase subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [P0CAP2](https://www.uniprot.org/uniprotkb/P0CAP2) (DNA-directed RNA polymerase II subunit GRINL1A):

> [Isoform 1]: Appears to be a stable component of the Pol II(G) complex form of RNA polymerase II (Pol II). Pol II synthesizes mRNA precursors and many functional non-coding RNAs and is the central component of the basal RNA polymerase II transcription machinery. May play a role in the Mediator complex-dependent regulation of transcription activation. Acts as a negative regulator of transcriptional activation; this repression is relieved by the Mediator complex, which restores Pol II(G) …

**Summary**, from NCBI Gene [81488](https://www.ncbi.nlm.nih.gov/gene/81488):

> This gene encodes a subunit of a specific form of RNA polymerase II termed Pol II(G). The encoded protein may act as a negative regulator of transcriptional activation by the Mediator complex. Alternative splicing results in multiple transcript variants. There is a pseudogene for this gene on chromosome 4. Readthrough transcription between this gene and the neighboring upstream gene MYZAP (myocardial zonula adherens protein) is represented with GeneID 145781. [provided by RefSeq, Oct 2013]

**Accessions** — [HGNC:14862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14862) · Entrez [81488](https://www.ncbi.nlm.nih.gov/gene/81488) · UniProt [P0CAP2](https://www.uniprot.org/uniprotkb/P0CAP2) · Ensembl [ENSG00000255529](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255529)

## Data

Gene col 14945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14945); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14945]; `tensor/DDL_lfc|DDL_z.npy` [14945]; `embed/gene_vectors.npy` [14945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14945 or target_col == 14945). Every well: [[POLR2M — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2M.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
