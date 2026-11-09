---
symbol: "SMIM19"
type: "gene"
col: 10697
ensembl_id: "ENSG00000176209"
name: "small integral membrane protein 19"
location: "8p11.21"
module: 10
arm: "+"
pooled_cpm: 12.38
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SMIM19

*small integral membrane protein 19* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.02× (z +10.7, q 8e-24, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.496× (z -7.4, q 6e-11, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WAC-AS1]] (+0.78, fdr 7e-06), [[SENP8]] (+0.77, fdr 1e-05), [[F8]] (+0.74, fdr 2e-05); moves opposite to [[USP35]] (-0.67, fdr 1e-05), [[CAMK2G]] (-0.64, fdr 5e-05), [[ST6GALNAC4]] (-0.64, fdr 5e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CBX2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RNF170]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +10.7 | 8e-24 | 41/45 (AsPC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +8.2 | 6e-14 | 23/24 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +8.2 | 6e-14 | 32/38 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +8.0 | 2e-13 | 26/30 (HEC-1-A, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.011 | 22/46 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.40×** | +3.6 | 0.024 | 18/42 (NCI-H1573, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.024 | 18/46 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.028 | 16/46 (A-172, A-427, …) | inconsistent across doses |  |
| [[Resveratrol (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.056 | 13/48 (CHP-212, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.496×** | -7.4 | 6e-11 | 33/47 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.501×** | -7.3 | 7e-11 | 34/46 (LS 180, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.525×** | -6.4 | 2e-08 | 32/46 (MIA PaCa-2, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.546×** | -6.4 | 2e-08 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.634×** | -4.8 | 2e-04 | 25/46 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.639×** | -4.7 | 2e-04 | 28/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.662×** | -4.3 | 0.001 | 28/48 (RKO, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.472×** | -4.1 | 0.003 | 22/43 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.483×** | -4.0 | 0.004 | 16/34 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.689×** | -3.9 | 0.005 | 22/47 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.696×** | -3.8 | 0.007 | 16/46 (LoVo, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -3.6 | 0.014 | 24/46 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.721×** | -3.4 | 0.026 | 18/47 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -3.3 | 0.034 | 12/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.741×** | -3.1 | 0.062 | 15/48 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 18.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 15.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -9.5) |
| [[A-172 (line)]] | wt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 7.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 7.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +8.5) | — |
| [[H4 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0664× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0667× (z -9.4) |
| [[HS-578T (line)]] | alt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 5.77 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.131× (z -8.8) |
| [[J82 (line)]] | alt | 14.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.213× (z -9.2) |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 9.02 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WAC-AS1]] | +0.78 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SENP8]] | +0.77 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[F8]] | +0.74 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[RWDD2B]] | +0.73 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[TIGD6]] | +0.73 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[HHLA3]] | +0.73 | +0.74 / +0.45 | both halves | 3e-05 |  |
| [[ERCC6L2-AS1]] | +0.71 | +0.78 / +0.27 | both halves | 3e-04 |  |
| [[TRAM2-AS1]] | +0.71 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[COQ5]] | +0.71 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[OARD1]] | +0.71 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[BCDIN3D]] | +0.71 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[RXYLT1]] | +0.70 | +0.70 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP35]] | -0.67 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[CAMK2G]] | -0.64 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[ST6GALNAC4]] | -0.64 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[PIP4K2A]] | -0.63 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[SH3PXD2B]] | -0.63 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[LPCAT4]] | -0.63 | -0.68 / -0.32 | both halves | 2e-04 |  |
| [[LPCAT1]] | -0.62 | -0.66 / -0.31 | both halves | 2e-04 |  |
| [[MAST3]] | -0.62 | -0.54 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CBX2]] | B | CBX2 activity raises SMIM19's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without CBX2 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SMIM19's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF170]] | C | SMIM19's natural level strengthens RNF170's drug response | SMIM19's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.14; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.2, 13.7); signed map (22.2, -14.6). **Vector** length 68.6, 13.1% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -4.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:42,541,155-42,555,195 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C8orf40 |
| Matched by | ensembl_id |

UniProt [Q96E16](https://www.uniprot.org/uniprotkb/Q96E16) carries no function annotation.

**Summary**, from NCBI Gene [114926](https://www.ncbi.nlm.nih.gov/gene/114926):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25166) · Entrez [114926](https://www.ncbi.nlm.nih.gov/gene/114926) · UniProt [Q96E16](https://www.uniprot.org/uniprotkb/Q96E16) · Ensembl [ENSG00000176209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176209)

## Data

Gene col 10697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10697); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10697]; `tensor/DDL_lfc|DDL_z.npy` [10697]; `embed/gene_vectors.npy` [10697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10697 or target_col == 10697). Every well: [[SMIM19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
