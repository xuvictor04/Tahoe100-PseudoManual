---
symbol: "RHBDD3"
type: "gene"
col: 1906
ensembl_id: "ENSG00000100263"
name: "rhomboid domain containing 3"
location: "22q12.2"
module: 64
arm: "+"
pooled_cpm: 9.75
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# RHBDD3

*rhomboid domain containing 3* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.40× (z +16.4, q 0e+00, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.673× (z -5.3, q 7e-05, down in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.154×); [[Thymol (drug)]] 0.5 µM in 1 line (C32 0.0852×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (CFPAC-1 0.0721×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCC1L]] (+0.72, fdr 5e-05), [[FBXO30]] (+0.71, fdr 4e-05), [[IGHMBP2]] (+0.71, fdr 1e-05); moves opposite to [[EFHC1]] (-0.59, fdr 1e-04), [[ARL3]] (-0.56, fdr 4e-04), [[GUSBP18]] (-0.56, fdr 6e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +16.4 | 0e+00 | 40/45 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.49×** | +15.7 | 0e+00 | 43/45 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.12×** | +15.1 | 0e+00 | 44/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.04×** | +14.7 | 0e+00 | 43/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.52×** | +12.3 | 2e-32 | 43/47 (LoVo, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +10.6 | 3e-24 | 27/45 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +9.9 | 4e-21 | 35/45 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +9.9 | 5e-21 | 29/43 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +7.1 | 6e-11 | 28/45 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +7.1 | 9e-11 | 25/41 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +6.8 | 5e-10 | 26/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.49×** | +6.3 | 1e-08 | 18/33 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.3 | 1e-08 | 22/48 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.89×** | +6.0 | 7e-08 | 23/48 (NCI-H2347, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.0 | 8e-08 | 25/45 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +5.3 | 3e-06 | 20/47 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.85×** | +4.3 | 5e-04 | 9/38 (HT-29, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1906.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.154×); [[Thymol (drug)]] 0.5 µM in 1 line (C32 0.0852×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (CFPAC-1 0.0721×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.673×** | -5.3 | 7e-05 | 20/47 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.695×** | -4.9 | 3e-04 | 17/47 (NCI-H1573, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.621× | -3.3 | 0.12 | 9/47 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.782× | -3.3 | 0.12 | 15/47 (SW48, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM |  | 0.709× | -3.3 | 0.12 | 3/48 (LS 180, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.0 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +8.9) | — |
| [[LoVo (line)]] | wt | 11.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 5.98× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 14.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +8.7) | — |
| [[KATO III (line)]] | alt | 15.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 20.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.43× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 1 | — | [[Asciminib (drug)]] 0.05 µM 0.115× (z -8.8) |
| [[C32 (line)]] | wt | 6.99 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0852× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 3.66 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0721× (z -9.0) |
| [[HS-578T (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 9.97 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.83× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.57 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 5.40 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.01× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 10.3 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.66× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +9.9) | — |
| [[A-172 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCC1L]] | +0.72 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[FBXO30]] | +0.71 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[IGHMBP2]] | +0.71 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[HTATIP2]] | +0.70 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[PSMB5]] | +0.69 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ALOX12P2-1]] | +0.68 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[MRPL45]] | +0.68 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[TIRAP]] | +0.67 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[AIFM2]] | +0.67 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[BAG2]] | +0.67 | +0.73 / +0.32 | both halves | 2e-04 |  |
| [[TYW3]] | +0.66 | +0.76 / +0.39 | both halves | 5e-05 |  |
| [[NSMAF]] | +0.66 | +0.59 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFHC1]] | -0.59 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[ARL3]] | -0.56 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[GUSBP18]] | -0.56 | -0.53 / -0.22 | both halves | 6e-04 |  |
| [[PIBF1]] | -0.56 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[ORC4]] | -0.56 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ARL6IP6]] | -0.55 | -0.48 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RHBDD3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers RHBDD3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IGFBP2]] | B | IGFBP2 activity raises RHBDD3's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without IGFBP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-16.4, 11.0); signed map (21.3, -24.8). **Vector** length 93.5, 19.8% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *proteasome* (control, mean cos +0.52 to 9); *Vif-mediated degradation of APOBEC3G* (reactome, mean cos +0.52 to 9); *Hedgehog 'on' state* (reactome, mean cos +0.50 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.4 | +14.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.0 | +15.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.3 | +15.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +16.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +6.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +4.3 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.8 | -5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.5 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | -4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | rhomboid domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,259,872-29,268,209 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTAG; previously C22orf3 |
| Gene groups (HGNC) | Rhomboid family |
| Matched by | ensembl_id |

UniProt [Q9Y3P4](https://www.uniprot.org/uniprotkb/Q9Y3P4) carries no function annotation.

**Summary**, from NCBI Gene [25807](https://www.ncbi.nlm.nih.gov/gene/25807):

> Predicted to enable serine-type endopeptidase activity. Predicted to act upstream of or within several processes, including liver development; negative regulation of natural killer cell activation; and positive regulation of protein catabolic process. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1308) · Entrez [25807](https://www.ncbi.nlm.nih.gov/gene/25807) · UniProt [Q9Y3P4](https://www.uniprot.org/uniprotkb/Q9Y3P4) · Ensembl [ENSG00000100263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100263)

## Data

Gene col 1906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1906); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1906]; `tensor/DDL_lfc|DDL_z.npy` [1906]; `embed/gene_vectors.npy` [1906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1906 or target_col == 1906). Every well: [[RHBDD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHBDD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
