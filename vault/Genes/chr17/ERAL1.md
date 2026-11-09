---
symbol: "ERAL1"
type: "gene"
col: 5343
ensembl_id: "ENSG00000132591"
name: "Era like 12S mitochondrial rRNA chaperone 1"
location: "17q11.2"
module: 7
arm: "+"
pooled_cpm: 9.78
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ERAL1

*Era like 12S mitochondrial rRNA chaperone 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.12× (z +9.8, q 5e-20, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.645× (z -6.0, q 1e-06, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUNDC1]] (+0.77, fdr 7e-06), [[SLC35A4]] (+0.73, fdr 7e-06), [[ASNSD1]] (+0.72, fdr 7e-06); moves opposite to [[ARPC1B]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PSMD4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5343.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +9.8 | 5e-20 | 36/45 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +9.2 | 8e-18 | 35/44 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +9.0 | 5e-17 | 36/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.59×** | +9.0 | 5e-17 | 32/45 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +8.0 | 1e-13 | 28/48 (CFPAC-1, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.58×** | +6.0 | 2e-07 | 10/20 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +5.6 | 2e-06 | 25/47 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.42×** | +4.8 | 1e-04 | 14/39 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.7 | 2e-04 | 14/44 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.6 | 2e-04 | 15/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.34×** | +4.0 | 0.004 | 12/33 (A498, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.004 | 9/47 (HOP62, J82, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.006 | 17/47 (HOP62, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.33×** | +3.7 | 0.008 | 13/44 (CFPAC-1, A498, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +3.6 | 0.011 | 6/47 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.012 | 11/48 (HS-578T, A549, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.016 | 3/44 (A549, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.018 | 12/45 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.60×** | +3.4 | 0.023 | 4/38 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.50×** | +2.9 | 0.098 | 0/39 | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5343.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -6.0 | 1e-06 | 22/47 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.792×** | -4.5 | 0.002 | 13/48 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.736×** | -4.2 | 0.006 | 19/47 (LS 180, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.754×** | -3.8 | 0.017 | 16/46 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.757×** | -3.8 | 0.017 | 13/45 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.763×** | -3.7 | 0.023 | 13/46 (hTERT-HPNE, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.766×** | -3.6 | 0.023 | 10/47 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.791× | -3.2 | 0.10 | 10/45 (NCI-H2030, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.801× | -3.0 | 0.16 | 20/45 (SHP-77, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0956× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.104× (z -9.3) |
| [[PANC-1 (line)]] | alt | 12.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0772× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUNDC1]] | +0.77 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[SLC35A4]] | +0.73 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[ASNSD1]] | +0.72 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[METTL18]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[MRPL35]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 | pathway: Mitochondrial ribosome-associated quality control |
| [[ACTR8]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.70 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[PPIE]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[INTS14]] | +0.69 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[ZNF845]] | +0.68 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[ZXDB]] | +0.68 | +0.78 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC1B]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ERAL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ERAL1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMD4]] | C | ERAL1's natural level strengthens PSMD4's drug response | ERAL1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.06; direction not clear | 0.039 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-33.8, 12.6); signed map (3.5, -30.4). **Vector** length 72.0, 12.6% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +9.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.6 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.7 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.1 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | Era like 12S mitochondrial rRNA chaperone 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,855,010-28,861,061 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HERA-B |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75616](https://www.uniprot.org/uniprotkb/O75616) (GTPase Era, mitochondrial):

> Probable GTPase that plays a role in the mitochondrial ribosomal small subunit assembly. Specifically binds the 12S mitochondrial rRNA (12S mt-rRNA) to a 33 nucleotide section delineating the 3' terminal stem-loop region. May act as a chaperone that protects the 12S mt-rRNA on the 28S mitoribosomal subunit during ribosomal small subunit assembly.

**Summary**, from NCBI Gene [26284](https://www.ncbi.nlm.nih.gov/gene/26284):

> The protein encoded by this gene is a GTPase that localizes to the mitochondrion. The encoded protein binds to the 3' terminal stem loop of 12S mitochondrial rRNA and is required for proper assembly of the 28S small mitochondrial ribosomal subunit. Deletion of this gene has been shown to cause mitochondrial dysfunction, growth retardation, and apoptosis. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:3424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3424) · Entrez [26284](https://www.ncbi.nlm.nih.gov/gene/26284) · UniProt [O75616](https://www.uniprot.org/uniprotkb/O75616) · Ensembl [ENSG00000132591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132591)

## Data

Gene col 5343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5343); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5343]; `tensor/DDL_lfc|DDL_z.npy` [5343]; `embed/gene_vectors.npy` [5343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5343 or target_col == 5343). Every well: [[ERAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
