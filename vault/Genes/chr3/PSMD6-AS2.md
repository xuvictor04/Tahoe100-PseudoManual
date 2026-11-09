---
symbol: "PSMD6-AS2"
type: "gene"
col: 14204
ensembl_id: "ENSG00000239653"
name: "PSMD6 antisense RNA 2"
location: "3p14.1"
module: 23
arm: "+"
pooled_cpm: 17.25
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PSMD6-AS2

*PSMD6 antisense RNA 2* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +10.2, q 1e-21, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.370× (z -14.2, q 6e-43, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD6-AS1]] (+0.76, fdr 1e-05, ⚠ same locus), [[CASS4]] (+0.75, fdr 1e-05), [[MCF2]] (+0.74, fdr 1e-05), [[DARS1-AS1]] (+0.73, fdr 7e-06); moves opposite to [[MRPS31P4]] (-0.64, fdr 1e-05), [[MAST3]] (-0.62, fdr 5e-05), [[STARD3NL]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +10.2 | 1e-21 | 36/47 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +7.9 | 8e-13 | 34/46 (LOX-IMVI, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.1 | 2e-07 | 26/48 (SW1417, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +5.0 | 7e-05 | 24/48 (SW480, LoVo, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.022 | 7/44 (HOP62, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.031 | 11/47 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.049 | 10/47 (A549, CFPAC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.074 | 14/46 (SW480, SNU-423, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.2 | 0.074 | 0/48 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.086 | 7/48 (NCI-H1573, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.089 | 13/47 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.23× | +3.0 | 0.11 | 6/48 (NCI-H460, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14204.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.370×** | -14.2 | 6e-43 | 42/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.417×** | -13.1 | 5e-37 | 44/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.420×** | -13.1 | 1e-36 | 42/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.279×** | -10.0 | 1e-21 | 40/48 (LOX-IMVI, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.329×** | -8.7 | 2e-16 | 29/44 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.557×** | -8.4 | 4e-15 | 35/47 (NCI-H2030, C32, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.594×** | -7.8 | 4e-13 | 22/37 (NCI-H1573, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -6.3 | 3e-08 | 26/47 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.678×** | -5.5 | 2e-06 | 23/45 (C-33 A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -4.9 | 5e-05 | 22/47 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.694×** | -4.4 | 6e-04 | 16/48 (HCT15, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.738×** | -4.4 | 6e-04 | 18/47 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift |
| [[Selinexor (drug)]] 5 µM |  | **0.817×** | -4.3 | 7e-04 | 19/48 (C32, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -4.2 | 0.001 | 21/41 (NCI-H1573, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.759×** | -4.1 | 0.001 | 20/46 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.739×** | -4.0 | 0.002 | 15/47 (HOP62, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fumaric acid (drug)]] 5 µM |  | **0.783×** | -3.5 | 0.013 | 11/47 (BT-474, SW1417, …) | top dose only | plate-row cell shift; position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **0.668×** | -3.2 | 0.040 | 12/43 (NCI-H1573, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 37.2 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.152× (z -15.1) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.139× (z -8.7) |
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.312× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 41.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.171× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 25.6 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.197× (z -11.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.247× (z -10.1) |
| [[SW480 (line)]] | alt | 16.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -10.1) |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.133× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 22.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.347× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.193× (z -10.2) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Decitabine (drug)]] 0.05 µM 0.222× (z -9.1) |
| [[SW48 (line)]] | wt | 17.2 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0825× (z -9.5) |
| [[A549 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 7.14 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.112× (z -8.5) ⚠ toxic; unreliable plate only |
| [[C32 (line)]] | wt | 19.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.323× (z -8.5) |
| [[COLO 205 (line)]] | alt | 9.88 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.104× (z -9.1) |
| [[HCT15 (line)]] | alt | 29.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.219× (z -8.5) |
| [[J82 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H2030 (line)]] | alt | 14.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.194× (z -8.5) |
| [[A-172 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6-AS1]] | +0.76 | +0.83 / +0.53 | both halves | 1e-05 | same gene group; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CASS4]] | +0.75 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[MCF2]] | +0.74 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[DARS1-AS1]] | +0.73 | +0.62 / +0.68 | both halves | 7e-06 | same gene group |
| [[ANKRD17-DT]] | +0.70 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | +0.69 | +0.65 / +0.55 | both halves | 1e-05 | same gene group |
| [[CORIN]] | +0.68 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[FRZB]] | +0.68 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[LINC02936]] | +0.68 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.67 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[DNAI4]] | +0.67 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[CA3]] | +0.66 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ANKHD1-EIF4EBP3]] | +0.66 | +0.63 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | -0.64 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[MAST3]] | -0.62 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[STARD3NL]] | -0.62 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[NDUFA12]] | -0.61 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[BBS5]] | -0.60 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ELP1]] | -0.59 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[VTA1]] | -0.59 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[BRAT1]] | -0.59 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[THYN1]] | -0.58 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[ALAD]] | -0.58 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[SKIC3]] | -0.58 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[RAB3D]] | -0.58 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PSMD6-AS2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | PSMD6-AS2's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | PSMD6-AS2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.510 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (6.9, 7.3); signed map (18.9, 1.0). **Vector** length 95.6, 21.6% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -14.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.7 | -13.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.2 | -13.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -10.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.0 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -8.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | PSMD6 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.1 — chr3:64,004,022-64,012,148 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44125) · Entrez [100507062](https://www.ncbi.nlm.nih.gov/gene/100507062) · Ensembl [ENSG00000239653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239653)

## Data

Gene col 14204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14204); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14204]; `tensor/DDL_lfc|DDL_z.npy` [14204]; `embed/gene_vectors.npy` [14204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14204 or target_col == 14204). Every well: [[PSMD6-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD6-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
