---
symbol: "AP4M1"
type: "gene"
col: 13308
ensembl_id: "ENSG00000221838"
name: "adaptor related protein complex 4 subunit mu 1"
location: "7q22.1"
module: 21
arm: "+"
pooled_cpm: 10.86
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# AP4M1

*adaptor related protein complex 4 subunit mu 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.38× (z +18.2, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.618× (z -7.2, q 5e-10, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPAT4-AS1]] (+0.55, fdr 1e-04), [[IFT140]] (+0.53, fdr 3e-05), [[PAN3]] (+0.53, fdr 4e-05); moves opposite to [[ZNF770]] (-0.54, fdr 1e-05), [[SRRD]] (-0.50, fdr 4e-04), [[FLNC]] (-0.50, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +18.2 | 0e+00 | 42/46 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +12.6 | 5e-34 | 11/19 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +12.1 | 3e-31 | 22/34 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +9.8 | 2e-20 | 21/29 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.008 | 13/46 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.064 | 10/40 (KATO III, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.073 | 9/44 (LS 180, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.3 | 0.073 | 13/45 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.2 | 0.076 | 10/40 (SW 900, HT-29, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Thymol (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.10 | 8/43 (NCI-H1573, SHP-77, …) | two highest doses |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.24× | +3.1 | 0.10 | 11/45 (hTERT-HPNE, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13308.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -7.2 | 5e-10 | 26/46 (RPMI-7951, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.688×** | -5.6 | 7e-06 | 20/47 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -5.2 | 4e-05 | 16/48 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.746×** | -4.4 | 0.002 | 17/46 (NCI-H23, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.764×** | -4.0 | 0.007 | 15/47 (SW48, A-427, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.795×** | -3.4 | 0.063 | 9/48 (NCI-H1792, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.805×** | -3.2 | 0.100 | 13/44 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.807×** | -3.2 | 0.100 | 15/47 (LOX-IMVI, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.0 | 0 | 2 (1 ⚠) | — | [[Penfluridol (drug)]] 5 µM 0.175× (z -10.7) |
| [[A498 (line)]] | wt | 14.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 7.55 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.29× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 13.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 5.67× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 7.22 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.80× (z +12.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 6.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +8.9) | — |
| [[C32 (line)]] | wt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +8.6) | — |
| [[J82 (line)]] | alt | 9.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 6.75 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0708× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 19.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.205× (z -9.4) |
| [[RKO (line)]] | wt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.0) | — |
| [[SW480 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +12.4) | — |
| [[A-427 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPAT4-AS1]] | +0.55 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[IFT140]] | +0.53 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[PAN3]] | +0.53 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[C12orf40]] | +0.53 | +0.23 / +0.56 | both halves | 5e-04 |  |
| [[C12orf57]] | +0.53 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[NFATC2IP-AS1]] | +0.53 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[ADNP-AS1]] | +0.52 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[NFKBID]] | +0.52 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[TICAM2-AS1]] | +0.52 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[PPP1R15B-AS1]] | +0.52 | +0.27 / +0.58 | both halves | 3e-04 |  |
| [[GEMIN7-AS1]] | +0.52 | +0.26 / +0.48 | both halves | 4e-04 |  |
| [[RAB11B-AS1]] | +0.52 | +0.35 / +0.57 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF770]] | -0.54 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[SRRD]] | -0.50 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[FLNC]] | -0.50 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[RANBP6]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PTPN11]] | -0.49 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[N6AMT1]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[MSANTD4]] | -0.48 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SYNJ2BP]] | -0.47 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[BBS10]] | -0.47 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[NUDT12]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[FEM1B]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[MSL3P1]] | -0.47 | -0.38 / -0.41 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises AP4M1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.6, 26.9); signed map (34.6, 2.7). **Vector** length 70.5, 11.5% of its response variance represented; |z| ≥ 3 in 799 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +18.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +12.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +12.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.4 | +1.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.4 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 4 subunit mu 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,100,858-100,110,345 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MU-ARP2, MU-4, SPG50 |
| Gene groups (HGNC) | Adaptor related protein complex 4 |
| Reactome | 4 pathways, smallest: Lysosome Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O00189](https://www.uniprot.org/uniprotkb/O00189) (AP-4 complex subunit mu-1):

> Component of the adaptor protein complex 4 (AP-4). Adaptor protein complexes are vesicle coat components involved both in vesicle formation and cargo selection. They control the vesicular transport of proteins in different trafficking pathways. AP-4 forms a non clathrin-associated coat on vesicles departing the trans-Golgi network (TGN) and may be involved in the targeting of proteins from the trans-Golgi network (TGN) to the endosomal-lysosomal system. It is also involved in protein sorting to …

**Summary**, from NCBI Gene [9179](https://www.ncbi.nlm.nih.gov/gene/9179):

> This gene encodes a subunit of the heterotetrameric AP-4 complex. The encoded protein belongs to the adaptor complexes medium subunits family. This AP-4 complex is involved in the recognition and sorting of cargo proteins with tyrosine-based motifs from the trans-golgi network to the endosomal-lysosomal system. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:574) · Entrez [9179](https://www.ncbi.nlm.nih.gov/gene/9179) · UniProt [O00189](https://www.uniprot.org/uniprotkb/O00189) · Ensembl [ENSG00000221838](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221838)

## Data

Gene col 13308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13308); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13308]; `tensor/DDL_lfc|DDL_z.npy` [13308]; `embed/gene_vectors.npy` [13308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13308 or target_col == 13308). Every well: [[AP4M1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP4M1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
