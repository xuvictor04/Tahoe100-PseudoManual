---
symbol: "BTN2A3P-1"
type: "gene"
col: 16584
ensembl_id: "ENSG00000291104"
name: ""
location: ""
module: 94
arm: "+"
pooled_cpm: 2.81
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# BTN2A3P-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.75× (z +15.6, q 0e+00, up in 27 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.439× (z -4.7, q 0.002, down in 14 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 0.0512×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0452×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.0992×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTN2A3P]] (+0.92, fdr 7e-06, ⚠ same locus), [[BTN2A2]] (+0.74, fdr 7e-06, ⚠ same locus), [[C7orf31]] (+0.67, fdr 2e-05), [[METTL18]] (+0.64, fdr 1e-05), [[PAXIP1-AS2]] (+0.62, fdr 1e-05); moves opposite to [[WRNIP1]] (-0.64, fdr 1e-05), [[NOMO1]] (-0.63, fdr 2e-05), [[CHID1]] (-0.63, fdr 1e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IRAG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16584.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.75×** | +15.6 | 0e+00 | 27/34 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.42×** | +9.2 | 7e-18 | 24/38 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +7.7 | 3e-12 | 17/33 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +7.0 | 4e-10 | 5/43 (J82, HOP62, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.03×** | +5.5 | 4e-06 | 2/9 (NCI-H2030, NCI-H460) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.8 | 2e-04 | 2/9 (A-172, HOP62) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +4.5 | 6e-04 | 12/36 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.004 | 8/42 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.004 | 4/44 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.004 | 4/38 (SK-MEL-2, J82, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.008 | 8/29 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.013 | 3/39 (HOP62, KATO III, …) | two highest doses |  |
| [[Valdecoxib (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.020 | 6/37 (SNU-423, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.029 | 2/39 (J82, NCI-H2030) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.039 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.039 | 6/42 (SW48, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.079 | 7/40 (A-172, BT-474, …) | two highest doses | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16584.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 0.0512×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0452×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.0992×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.439×** | -4.7 | 0.002 | 14/34 (NCI-H460, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.496×** | -4.0 | 0.018 | 8/31 (SNU-423, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 7.18 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0512× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[CFPAC-1 (line)]] | alt | 3.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 3.69 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0992× (z -9.0) ⚠ toxic |
| [[LoVo (line)]] | wt | 3.08 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0750× (z -8.6) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 4.31 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0452× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[A-172 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A3P]] | +0.92 | +0.93 / +0.82 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[BTN2A2]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 | ⚠ same locus (26.5 kb, same strand: neighbours can correlate without regulation) |
| [[C7orf31]] | +0.67 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[BTN2A1]] | +0.66 | +0.61 / +0.51 | both halves | 1e-05 | ⚠ same locus (25.5 kb, same strand: neighbours can correlate without regulation) |
| [[METTL18]] | +0.64 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[PAXIP1-AS2]] | +0.62 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[ZNF563]] | +0.62 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[ARL14EP]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[STAP2]] | +0.61 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[CCDC102A]] | +0.60 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[CASP7]] | +0.60 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[OCIAD1]] | +0.59 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[ZC3HC1]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SNRNP27]] | +0.59 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[TRAF3IP2]] | +0.59 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRNIP1]] | -0.64 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[NOMO1]] | -0.63 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[CHID1]] | -0.63 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.63 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[CTXN1]] | -0.61 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[COLGALT1]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[SLC25A39]] | -0.60 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[TBCD]] | -0.60 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PODXL2]] | -0.60 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[SETD3]] | -0.60 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[NUTF2]] | -0.58 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[MAPK1]] | -0.58 | -0.54 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAG2]] | B | IRAG2 activity raises BTN2A3P-1's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 1.38× lower at baseline in the lines without IRAG2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[BTN2A2]] | C | BTN2A2 activity raises BTN2A3P-1's level | lines that do not express BTN2A2 (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without BTN2A2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC18, TBKBP1, TTC23L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.3, 6.7); signed map (18.1, -13.5). **Vector** length 50.9, 6.41% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +7.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.3 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.9 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +3.3 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.6 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | +0.8 |

## What is on record

> [!warning] No registry record
> BTN2A3P-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16584); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16584]; `tensor/DDL_lfc|DDL_z.npy` [16584]; `embed/gene_vectors.npy` [16584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16584 or target_col == 16584). Every well: [[BTN2A3P-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTN2A3P-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
