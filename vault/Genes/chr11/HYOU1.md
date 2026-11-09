---
symbol: "HYOU1"
type: "gene"
col: 7373
ensembl_id: "ENSG00000149428"
name: "hypoxia up-regulated 1"
location: "11q23.3"
module: 42
arm: "+"
pooled_cpm: 135.64
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# HYOU1

*hypoxia up-regulated 1* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +12.7, q 4e-34, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +9.9, q 7e-21, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.624× (z -5.8, q 4e-06, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJB11]] (+0.82, fdr 7e-06), [[PDIA4]] (+0.81, fdr 7e-06), [[SEC61A1]] (+0.80, fdr 7e-06); moves opposite to [[EID2]] (-0.57, fdr 3e-05), [[CMTR2]] (-0.56, fdr 4e-05), [[GPATCH8]] (-0.56, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CTH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7373.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.69×** | +12.7 | 4e-34 | 46/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +10.8 | 2e-24 | 40/43 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +9.9 | 7e-21 | 42/48 (AsPC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +8.4 | 6e-15 | 41/47 (LOX-IMVI, A-172, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +8.4 | 6e-15 | 38/44 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.65×** | +6.4 | 2e-08 | 37/47 (LOX-IMVI, SW480, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.54×** | +5.6 | 2e-06 | 30/47 (LOX-IMVI, SW480, …) | two highest doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.50×** | +5.0 | 4e-05 | 33/49 (LOX-IMVI, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +4.7 | 2e-04 | 31/47 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.44×** | +4.6 | 2e-04 | 29/47 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.011 | 26/47 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.6 | 0.017 | 19/37 (HOP62, AsPC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Lipoic acid (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.017 | 21/47 (PANC-1, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.036 | 23/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.2 | 0.050 | 21/44 (SW 900, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.624×** | -5.8 | 4e-06 | 36/47 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.726×** | -5.0 | 1e-04 | 32/47 (A-427, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.686×** | -4.8 | 3e-04 | 35/47 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.648×** | -4.7 | 5e-04 | 31/47 (A-427, HS-578T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.716×** | -4.3 | 0.002 | 27/47 (A-427, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.734×** | -3.6 | 0.024 | 26/46 (HS-578T, A-172, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.744×** | -3.6 | 0.024 | 28/48 (H4, NCI-H2030, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.761×** | -3.4 | 0.057 | 23/46 (A498, SNU-423, …) | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.743×** | -3.2 | 0.084 | 23/48 (HCT15, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **0.805×** | -3.2 | 0.084 | 26/47 (H4, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.824×** | -3.1 | 0.085 | 23/47 (RKO, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Berbamine (drug)]] 0.05 µM |  | 0.754× | -3.0 | 0.11 | 22/47 (HT-29, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 70.2 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +11.0) | — |
| [[A-427 (line)]] | wt | 83.3 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0599× (z -25.6) |
| [[A-172 (line)]] | wt | 109 | 2 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 2.47× (z +9.4) | [[Harringtonine (drug)]] 5 µM 0.408× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 202 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.407× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 88.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +11.3) | — |
| [[SW480 (line)]] | alt | 89.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 99.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.8) | — |
| [[KATO III (line)]] | alt | 510 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.268× (z -11.3) |
| [[SNU-423 (line)]] | alt | 64.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 74.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 56.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +12.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 221 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -14.3) |
| [[A498 (line)]] | wt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 266 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -12.8) |
| [[J82 (line)]] | alt | 117 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +10.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 163 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +13.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 117 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.16× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 147 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 151 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 304 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 107 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.1) | — |
| [[RKO (line)]] | wt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -17.6) |
| [[SW 1271 (line)]] | alt | 104 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0996× (z -10.4) |
| [[SW48 (line)]] | wt | 112 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.8) | — |
| [[A549 (line)]] | wt | 32.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 166 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 111 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 114 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 96.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB11]] | +0.82 | +0.78 / +0.80 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 976 |
| [[PDIA4]] | +0.81 | +0.79 / +0.85 | both halves | 7e-06 | STRING 997 |
| [[SEC61A1]] | +0.80 | +0.82 / +0.76 | both halves | 7e-06 | STRING 806 |
| [[SEL1L]] | +0.80 | +0.81 / +0.82 | both halves | 7e-06 | STRING 854 |
| [[CANX]] | +0.77 | +0.80 / +0.76 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 869 |
| [[PDIA6]] | +0.76 | +0.72 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 943 |
| [[HSP90B1]] | +0.76 | +0.76 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 999 |
| [[TMED2]] | +0.76 | +0.75 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[DNAJC3]] | +0.75 | +0.78 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 928 |
| [[PDIA3]] | +0.74 | +0.71 / +0.78 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 877 |
| [[HSPA5]] | +0.74 | +0.80 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 999 |
| [[MANF]] | +0.74 | +0.81 / +0.69 | both halves | 7e-06 | STRING 726 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EID2]] | -0.57 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[CMTR2]] | -0.56 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[GPATCH8]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[TGIF2]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTH]] | B | CTH activity raises HYOU1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without CTH | 0.063 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[SARS1]] | C | SARS1's natural level weakens HYOU1's drug response | SARS1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.36; direction not clear | 0.008 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CKAP4]] | C | CKAP4 activity raises HYOU1's level | lines that do not express CKAP4 (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without CKAP4 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CAMKK1; maybe low, not absent; its own permutation p |
| [[HSPA5]] | C | HSPA5's natural level weakens HYOU1's drug response | HSPA5's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.23; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.851). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, -30.6); signed map (-54.9, 7.5). **Vector** length 148, 52.2% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.56 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.51 to 13); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.51 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +12.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.7 | +5.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +0.7 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +2.4 | +2.2 |
|  | [[Dihydroartemisinin (drug)]] 0.5 µM |  | +2.4 | +1.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.8 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.0 | -4.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.8 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -3.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -3.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.6 | -3.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | hypoxia up-regulated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,044,188-119,057,227 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ORP150, HSP12A, Grp170 |
| Gene groups (HGNC) | Heat shock 70kDa proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 12 pathways, smallest: Scavenging by Class F Receptors; Binding and Uptake of Ligands by Scavenger Receptors; XBP1(S) activates chaperone genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4L1](https://www.uniprot.org/uniprotkb/Q9Y4L1) (Hypoxia up-regulated protein 1):

> Has a pivotal role in cytoprotective cellular mechanisms triggered by oxygen deprivation. Promotes HSPA5/BiP-mediated ATP nucleotide exchange and thereby activates the unfolded protein response (UPR) pathway in the presence of endoplasmic reticulum stress (By similarity). May play a role as a molecular chaperone and participate in protein folding.

**Summary**, from NCBI Gene [10525](https://www.ncbi.nlm.nih.gov/gene/10525):

> The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in protein folding and secretion in the ER. Since suppression of the protein is associated with accelerated …

**Accessions** — [HGNC:16931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16931) · Entrez [10525](https://www.ncbi.nlm.nih.gov/gene/10525) · UniProt [Q9Y4L1](https://www.uniprot.org/uniprotkb/Q9Y4L1) · Ensembl [ENSG00000149428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149428)

## Data

Gene col 7373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7373); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7373]; `tensor/DDL_lfc|DDL_z.npy` [7373]; `embed/gene_vectors.npy` [7373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7373 or target_col == 7373). Every well: [[HYOU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HYOU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
