---
symbol: "PRR14"
type: "gene"
col: 8018
ensembl_id: "ENSG00000156858"
name: "proline rich 14"
location: "16p11.2"
module: 14
arm: "+"
pooled_cpm: 9.95
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PRR14

*proline rich 14* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.74× (z +24.0, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.735× (z -4.0, q 0.039, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (CFPAC-1 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change); [[Silodosin (drug)]] 5 µM in 1 line (NCI-H2030 0.237×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SW 900 0.0992×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR108]] (+0.73, fdr 7e-06), [[PBX2]] (+0.72, fdr 9e-06), [[AMZ2P1-1]] (+0.71, fdr 7e-06); moves opposite to [[TXN]] (-0.57, fdr 1e-05), [[SENP5]] (-0.56, fdr 2e-05), [[MFN1]] (-0.52, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLEKHG4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.74×** | +24.0 | 0e+00 | 41/45 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.66×** | +19.2 | 0e+00 | 43/46 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +7.9 | 6e-13 | 26/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +7.4 | 1e-11 | 27/39 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +7.4 | 1e-11 | 32/47 (PANC-1, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +5.8 | 7e-07 | 24/41 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.4 | 4e-06 | 20/46 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.6 | 3e-04 | 21/46 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +4.6 | 3e-04 | 17/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +4.1 | 0.003 | 14/43 (MIA PaCa-2, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.059 | 12/48 (J82, MIA PaCa-2, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.2 | 0.059 | 10/38 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8018.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (CFPAC-1 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change); [[Silodosin (drug)]] 5 µM in 1 line (NCI-H2030 0.237×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SW 900 0.0992×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -4.0 | 0.039 | 15/47 (NCI-H661, SW480, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.751×** | -3.7 | 0.061 | 10/46 (J82, A-427, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.842× | -3.1 | 0.37 | 11/48 (LoVo, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 9.55 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +18.5) | — |
| [[PANC-1 (line)]] | alt | 11.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +28.7) | — |
| [[A498 (line)]] | wt | 16.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +17.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +12.1) | [[Silodosin (drug)]] 5 µM 0.237× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 6.67 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +13.6) | — |
| [[A-172 (line)]] | wt | 16.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 7.40 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[J82 (line)]] | alt | 11.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +14.2) | — |
| [[NCI-H1573 (line)]] | alt | 8.48 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 7.56× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 7.12 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +9.6) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0992× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 6.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 8.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 4.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 7.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +9.0) | — |
| [[LoVo (line)]] | wt | 7.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 7.33 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 12.7× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 5.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 7.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 9.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 8.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.5) | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR108]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[PBX2]] | +0.72 | +0.74 / +0.57 | both halves | 9e-06 |  |
| [[AMZ2P1-1]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[DXO]] | +0.70 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[DEDD]] | +0.69 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[PLXNB2]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[BCL3]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[CIC]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[TEF]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[MBD6]] | +0.64 | +0.71 / +0.56 | both halves | 1e-05 | STRING 436 |
| [[SYNPO]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.63 | +0.68 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN]] | -0.57 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[SENP5]] | -0.56 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[MFN1]] | -0.52 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[HSPD1]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG4]] | B | PLEKHG4 activity lowers PRR14's level | lines that do not express PLEKHG4 (11) vs lines expressing it (39) | 1.24× higher at baseline in the lines without PLEKHG4 | 0.082 | ⚠ within organs, on part of the lines; also absent: SLC2A12, PPP1R1C, TMEM51-AS1 |
| [[KREMEN2]] | B | KREMEN2 activity raises PRR14's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.28× lower at baseline in the lines without KREMEN2 | 0.087 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.5, 4.8); signed map (11.4, -18.2). **Vector** length 74.1, 12.9% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +24.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +19.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.6 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +7.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.0 | +7.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.3 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,650,717-30,656,413 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3121 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWN1](https://www.uniprot.org/uniprotkb/Q9BWN1) (Proline-rich protein 14):

> Functions in tethering peripheral heterochromatin to the nuclear lamina during interphase, possibly through the interaction with heterochromatin protein CBX5/HP1 alpha. Might play a role in reattaching heterochromatin to the nuclear lamina at mitotic exit. Promotes myoblast differentiation during skeletal myogenesis, possibly by stimulating transcription factor MyoD activity via binding to CBX5/HP1 alpha. Involved in the positive regulation of the PI3K-Akt-mTOR signaling pathway and in …

**Summary**, from NCBI Gene [78994](https://www.ncbi.nlm.nih.gov/gene/78994):

> The protein encoded by this gene tethers heterochromatin to the nuclear laminar scaffold by binding heterochromatin protein 1 (HP1) and the nuclear lamina. The tether is broken during mitosis and reforms quickly after mitosis, with the encoded protein first binding HP1 and then attaching to the nuclear lamina. This protein also has been shown to promote MyoD activity and skeletal myogenesis. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:28458](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28458) · Entrez [78994](https://www.ncbi.nlm.nih.gov/gene/78994) · UniProt [Q9BWN1](https://www.uniprot.org/uniprotkb/Q9BWN1) · Ensembl [ENSG00000156858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156858)

## Data

Gene col 8018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8018); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8018]; `tensor/DDL_lfc|DDL_z.npy` [8018]; `embed/gene_vectors.npy` [8018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8018 or target_col == 8018). Every well: [[PRR14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
