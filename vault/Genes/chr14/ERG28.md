---
symbol: "ERG28"
type: "gene"
col: 5487
ensembl_id: "ENSG00000133935"
name: "ergosterol biosynthesis 28 homolog"
location: "14q24.3"
module: 86
arm: "+"
pooled_cpm: 11.85
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# ERG28

*ergosterol biosynthesis 28 homolog* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Berbamine (drug)]] 5 µM: 1.78× (z +9.1, q 4e-17, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.547× (z -6.8, q 5e-09, down in 28 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDFT1]] (+0.82, fdr 7e-06), [[MSMO1]] (+0.79, fdr 7e-06), [[HMGCR]] (+0.77, fdr 7e-06); moves opposite to [[NEPRO-AS1]] (-0.54, fdr 3e-05), [[GPATCH4]] (-0.53, fdr 3e-05), [[RPL7L1]] (-0.53, fdr 4e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[QPRT]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TTLL5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 5 µM |  | **1.78×** | +9.1 | 4e-17 | 39/47 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.74×** | +8.8 | 4e-16 | 34/47 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +8.7 | 8e-16 | 40/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.12×** | +8.4 | 4e-15 | 39/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +8.3 | 1e-14 | 39/46 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.15×** | +8.3 | 1e-14 | 13/19 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.98×** | +7.7 | 2e-12 | 23/36 (C32, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.75×** | +5.8 | 5e-07 | 17/28 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.65×** | +5.6 | 1e-06 | 26/46 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.52×** | +4.7 | 1e-04 | 26/46 (hTERT-HPNE, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +4.7 | 1e-04 | 17/44 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.40×** | +3.8 | 0.008 | 14/39 (CFPAC-1, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.7 | 0.010 | 6/23 (SW480, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.5 | 0.022 | 2/47 (HOP62, hTERT-HPNE) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.029 | 9/46 (NCI-H2030, C32, …) | top dose only | plate-row cell shift |
| [[Adagrasib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.029 | 9/46 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.038 | 10/46 (A549, HCT15, …) | top dose only | plate-row cell shift |
| [[Berbamine (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.046 | 11/45 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.046 | 10/46 (NCI-H2030, J82, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.046 | 9/43 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Posaconazole (drug)]] 5 µM |  | **1.31×** | +2.9 | 0.080 | 11/46 (BT-474, NCI-H2030, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5487.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.547×** | -6.8 | 5e-09 | 28/42 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.683×** | -6.1 | 2e-07 | 24/44 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.609×** | -5.6 | 4e-06 | 27/45 (BT-474, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.635×** | -5.1 | 4e-05 | 24/46 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.662×** | -4.7 | 3e-04 | 21/46 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.671×** | -4.5 | 6e-04 | 17/46 (KATO III, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.691×** | -3.9 | 0.008 | 20/43 (SW480, HT-29, …) | all doses, flat | low cells (technical?) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.592× | -3.1 | 0.12 | 8/47 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dabrafenib (drug)]] 5 µM |  | 0.593× | -3.1 | 0.12 | 9/47 (KATO III, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 26.9 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 3.26× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.7) |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -8.6) |
| [[SW480 (line)]] | alt | 13.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.94× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -10.6) |
| [[A549 (line)]] | wt | 7.55 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 8.06 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.249× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 11.6 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 3.70× (z +9.5) | — |
| [[A-172 (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDFT1]] | +0.82 | +0.83 / +0.72 | both halves | 7e-06 | STRING 984 |
| [[MSMO1]] | +0.79 | +0.78 / +0.75 | both halves | 7e-06 | STRING 994 |
| [[HMGCR]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 | STRING 550 |
| [[SLC25A1]] | +0.77 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[SREBF2]] | +0.76 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[MVD]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 | STRING 466 |
| [[FDPS]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 | STRING 451 |
| [[DHCR7]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 | STRING 915 |
| [[SCD]] | +0.72 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[EBP]] | +0.69 | +0.71 / +0.59 | both halves | 7e-06 | STRING 580 |
| [[ACSS2]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[SQLE]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 | STRING 710 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEPRO-AS1]] | -0.54 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[GPATCH4]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[RPL7L1]] | -0.53 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ZNF562]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[NOP14]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[CYREN]] | -0.51 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[UTP3]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ZNF121]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PPP1R1C]] | -0.50 | -0.38 / -0.47 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[QPRT]] | B | QPRT activity raises ERG28's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.23× lower at baseline in the lines without QPRT | 0.049 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTLL5]] | C | ERG28's natural level strengthens TTLL5's drug response | ERG28's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.15; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.5, -48.6); signed map (-53.3, 32.0). **Vector** length 90.8, 20.3% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.65 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.67 to 20); *cholesterol homeostasis* (hallmark, mean cos +0.64 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +4.8 | +8.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +4.7 | +9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +8.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +8.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.1 | +5.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +3.0 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | ergosterol biosynthesis 28 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,649,791-75,660,876 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NET51; previously C14orf1 |
| Matched by | ensembl_id |

UniProt [Q9UKR5](https://www.uniprot.org/uniprotkb/Q9UKR5) carries no function annotation.

**Summary**, from NCBI Gene [11161](https://www.ncbi.nlm.nih.gov/gene/11161):

> Enables identical protein binding activity. Predicted to be involved in sterol biosynthetic process. Located in transport vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1187) · Entrez [11161](https://www.ncbi.nlm.nih.gov/gene/11161) · UniProt [Q9UKR5](https://www.uniprot.org/uniprotkb/Q9UKR5) · Ensembl [ENSG00000133935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133935)

## Data

Gene col 5487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5487); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5487]; `tensor/DDL_lfc|DDL_z.npy` [5487]; `embed/gene_vectors.npy` [5487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5487 or target_col == 5487). Every well: [[ERG28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERG28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
