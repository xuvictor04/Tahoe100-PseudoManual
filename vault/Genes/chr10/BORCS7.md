---
symbol: "BORCS7"
type: "gene"
col: 9276
ensembl_id: "ENSG00000166275"
name: "BLOC-1 related complex subunit 7"
location: "10q24.32"
module: 23
arm: "+"
pooled_cpm: 16.09
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# BORCS7

*BLOC-1 related complex subunit 7* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.60× (z +15.9, q 0e+00, up in 40 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +6.2, q 7e-08, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.576× (z -6.8, q 3e-09, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BORCS7-ASMT]] (+0.66, fdr 3e-05, ⚠ same locus), [[USP34-DT]] (+0.65, fdr 3e-05), [[KMT2E-AS1]] (+0.65, fdr 3e-05), [[CYB5D2]] (+0.64, fdr 1e-05); moves opposite to [[PAQR4]] (-0.56, fdr 1e-05), [[GNB1L]] (-0.56, fdr 7e-05), [[LPCAT1]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9276.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.60×** | +15.9 | 0e+00 | 40/42 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.34×** | +14.4 | 8e-45 | 29/30 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +11.2 | 5e-27 | 33/37 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +6.9 | 8e-10 | 32/44 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.2 | 7e-08 | 27/47 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.9 | 1e-04 | 23/47 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **1.36×** | +3.8 | 0.011 | 20/46 (HepG2/C3A, SW48, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.051 | 7/45 (NCI-H460, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.48×** | +3.3 | 0.051 | 16/45 (HCT15, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.11 | 13/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.28× | +3.1 | 0.11 | 13/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9276.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.576×** | -6.8 | 3e-09 | 33/48 (NCI-H460, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.577×** | -6.8 | 3e-09 | 33/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.603×** | -6.3 | 7e-08 | 30/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.613×** | -6.1 | 2e-07 | 31/48 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.699×** | -4.4 | 0.001 | 22/48 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.560×** | -3.8 | 0.016 | 14/48 (NCI-H460, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 17.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.41× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 13.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +8.8) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0808× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 17.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.61× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +10.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 15.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.23× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +11.6) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.156× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 24.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 18.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 15.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +8.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0838× (z -9.3) |
| [[HT-29 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 15.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0959× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~66% of this change |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 7 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BORCS7-ASMT]] | +0.66 | +0.62 / +0.45 | both halves | 3e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[USP34-DT]] | +0.65 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[KMT2E-AS1]] | +0.65 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[CYB5D2]] | +0.64 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[AS3MT]] | +0.64 | +0.54 / +0.46 | both halves | 3e-05 | STRING 851; ⚠ same locus (4.5 kb, same strand: neighbours can correlate without regulation) |
| [[GTF2IRD2]] | +0.63 | +0.60 / +0.38 | both halves | 7e-05 |  |
| [[MR1]] | +0.63 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[UFC1]] | +0.63 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[C2CD5-AS1]] | +0.62 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[TRAF3IP2-AS1]] | +0.61 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[PNISR]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.61 | +0.62 / +0.23 | both halves | 5e-04 |  |
| [[EFCAB5]] | +0.60 | +0.51 / +0.29 | both halves | 2e-04 |  |
| [[EYS]] | +0.60 | +0.42 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAQR4]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[GNB1L]] | -0.56 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[LPCAT1]] | -0.56 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[FLNB]] | -0.55 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[MLX]] | -0.54 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[PPM1G]] | -0.54 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[SH2B2]] | -0.54 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[SLCO4A1]] | -0.53 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[CPTP]] | -0.53 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[ARF6]] | -0.53 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[STUB1]] | -0.53 | -0.34 / -0.16 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises BORCS7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (8.2, 22.5); signed map (29.6, -15.2). **Vector** length 75.5, 15.1% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +15.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.4 | +2.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +0.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | -6.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.5 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.4 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | BLOC-1 related complex subunit 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,854,259-102,864,961 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40752; previously C10orf32 |
| Gene groups (HGNC) | BLOC-1 related complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96B45](https://www.uniprot.org/uniprotkb/Q96B45) (BLOC-1-related complex subunit 7):

> As part of the BORC complex may play a role in lysosomes movement and localization at the cell periphery. Associated with the cytosolic face of lysosomes, the BORC complex may recruit ARL8B and couple lysosomes to microtubule plus-end-directed kinesin motor.

**Summary**, from NCBI Gene [119032](https://www.ncbi.nlm.nih.gov/gene/119032):

> Predicted to be involved in organelle transport along microtubule; regulation of endosome size; and regulation of lysosome size. Predicted to act upstream of or within several processes, including lysosome localization; motor behavior; and response to cycloheximide. Part of BORC complex. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:23516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23516) · Entrez [119032](https://www.ncbi.nlm.nih.gov/gene/119032) · UniProt [Q96B45](https://www.uniprot.org/uniprotkb/Q96B45) · Ensembl [ENSG00000166275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166275)

## Data

Gene col 9276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9276); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9276]; `tensor/DDL_lfc|DDL_z.npy` [9276]; `embed/gene_vectors.npy` [9276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9276 or target_col == 9276). Every well: [[BORCS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BORCS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
