---
symbol: "SEC24C"
type: "gene"
col: 10776
ensembl_id: "ENSG00000176986"
name: "SEC24 homolog C, COPII component"
location: "10q22.2"
module: 42
arm: "+"
pooled_cpm: 72.66
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SEC24C

*SEC24 homolog C, COPII component* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.55× (z +9.7, q 2e-19, up in 45 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (PANC-1 7.70×, KATO III 6.70×, HS-578T 6.39×, RPMI-7951 5.77×, …); [[PH-797804 (drug)]] 5 µM in 2 lines (PANC-1 5.73×, HS-578T 5.48×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.22×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 2.13×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.716× (z -6.9, q 1e-09, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH5]] (+0.73, fdr 7e-06), [[COPA]] (+0.73, fdr 7e-06), [[SAR1A]] (+0.73, fdr 7e-06); moves opposite to [[SLC25A13]] (-0.62, fdr 2e-05), [[CUX1]] (-0.59, fdr 4e-05), [[SH3D19]] (-0.59, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10776.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (PANC-1 7.70×, KATO III 6.70×, HS-578T 6.39×, RPMI-7951 5.77×, …); [[PH-797804 (drug)]] 5 µM in 2 lines (PANC-1 5.73×, HS-578T 5.48×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.22×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 2.13×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.55×** | +9.7 | 2e-19 | 45/49 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.78×** | +7.8 | 2e-12 | 40/48 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.26× | +3.4 | 0.13 | 24/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.1 | 0.26 | 0/50 | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.23× | +3.0 | 0.26 | 22/48 (A-172, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.716×** | -6.9 | 1e-09 | 31/48 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -6.9 | 1e-09 | 30/43 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.655×** | -6.2 | 1e-07 | 34/49 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.689×** | -5.0 | 6e-05 | 29/45 (SHP-77, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.710×** | -5.0 | 6e-05 | 30/48 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.802×** | -4.6 | 5e-04 | 30/48 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.736×** | -4.3 | 0.001 | 28/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **0.773×** | -3.6 | 0.020 | 26/47 (NCI-H2347, C-33 A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.794×** | -3.2 | 0.073 | 23/48 (J82, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 78.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -11.6) |
| [[PANC-1 (line)]] | alt | 78.4 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.70× (z +12.4) | — |
| [[A-172 (line)]] | wt | 75.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -11.6) |
| [[CHP-212 (line)]] | wt | 75.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Retinoic acid (drug)]] 0.5 µM 0.173× (z -9.5) |
| [[A-427 (line)]] | wt | 48.3 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.446× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 87.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -10.1) |
| [[HS-578T (line)]] | alt | 58.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.39× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 67.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0984× (z -16.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 44.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 92.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -16.6) |
| [[RKO (line)]] | wt | 84.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 80.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.77× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -8.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 46.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0775× (z -18.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 58.0 | 0 | 2 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0747× (z -9.1) |
| [[SW 900 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -14.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 76.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.17× (z +8.8) | — |
| [[A549 (line)]] | wt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -8.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 97.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -9.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 54.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.0) |
| [[H4 (line)]] | wt | 77.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -10.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 63.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.70× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 62.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -11.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 63.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 88.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 66.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -11.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 66.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.7) |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 86.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 92.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 99.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 88.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH5]] | +0.73 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[COPA]] | +0.73 | +0.78 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 627 |
| [[SAR1A]] | +0.73 | +0.78 / +0.63 | both halves | 7e-06 | same gene group; STRING 992 |
| [[SEC61A1]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 | STRING 606 |
| [[TMEM39A]] | +0.71 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[DDB1]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[NOMO2]] | +0.70 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[GORASP2]] | +0.70 | +0.75 / +0.66 | both halves | 7e-06 | STRING 430 |
| [[SEC13]] | +0.69 | +0.75 / +0.60 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[P4HB]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[STT3A]] | +0.69 | +0.76 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[COPG1]] | +0.68 | +0.70 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 831 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A13]] | -0.62 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[CUX1]] | -0.59 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[SH3D19]] | -0.59 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.2, -30.9); signed map (-52.9, 6.7). **Vector** length 101, 27.4% of its response variance represented; |z| ≥ 3 in 777 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.58 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.57 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.56 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +9.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +7.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -0.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.2 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | -3.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -2.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | +0.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | SEC24 homolog C, COPII component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,744,372-73,772,161 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0079 |
| Gene groups (HGNC) | Coat protein complex II |
| Reactome | 19 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; Cargo concentration in the ER; Regulation of cholesterol biosynthesis by SREBP (SREBF) |
| Matched by | ensembl_id |

**Function**, from UniProt [P53992](https://www.uniprot.org/uniprotkb/P53992) (Protein transport protein Sec24C):

> Component of the coat protein complex II (COPII) which promotes the formation of transport vesicles from the endoplasmic reticulum (ER). The coat has two main functions, the physical deformation of the endoplasmic reticulum membrane into vesicles and the selection of cargo molecules for their transport to the Golgi complex. Plays a central role in cargo selection within the COPII complex and together with SEC24D may have a different specificity compared to SEC24A and SEC24B. May more …

**Summary**, from NCBI Gene [9632](https://www.ncbi.nlm.nih.gov/gene/9632):

> The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The product of this gene may play a role in shaping the vesicle, as well as in cargo selection and concentration. Alternatively spliced transcript variants encoding the same protein have been identified. …

**Accessions** — [HGNC:10705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10705) · Entrez [9632](https://www.ncbi.nlm.nih.gov/gene/9632) · UniProt [P53992](https://www.uniprot.org/uniprotkb/P53992) · Ensembl [ENSG00000176986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176986)

## Data

Gene col 10776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10776); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10776]; `tensor/DDL_lfc|DDL_z.npy` [10776]; `embed/gene_vectors.npy` [10776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10776 or target_col == 10776). Every well: [[SEC24C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC24C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
