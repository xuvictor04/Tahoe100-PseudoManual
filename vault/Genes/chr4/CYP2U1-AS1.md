---
symbol: "CYP2U1-AS1"
type: "gene"
col: 14426
ensembl_id: "ENSG00000245293"
name: "CYP2U1 and SGMS2 antisense RNA 1"
location: "4q25"
module: 21
arm: "+"
pooled_cpm: 5.35
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CYP2U1-AS1

*CYP2U1 and SGMS2 antisense RNA 1* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.05× (z +16.3, q 0e+00, up in 46 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Phenytoin (sodium) (drug)]] 0.05 µM in 1 line (KATO III 0.0523×); [[Rosiglitazone (drug)]] 5 µM in 1 line (NCI-H1573 0.0735×); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0693×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETFBKMT]] (+0.64, fdr 1e-05), [[ATP6V1C2]] (+0.62, fdr 7e-06), [[SMPD3]] (+0.62, fdr 1e-05); moves opposite to [[CCT5]] (-0.50, fdr 1e-04), [[PROSER1]] (-0.49, fdr 5e-05), [[TSEN15]] (-0.48, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AMBP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.05×** | +16.3 | 0e+00 | 46/47 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.55×** | +14.8 | 0e+00 | 43/47 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.24×** | +13.7 | 2e-40 | 39/46 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +13.1 | 4e-37 | 37/42 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +9.8 | 1e-20 | 25/38 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.24×** | +9.4 | 4e-19 | 19/28 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.88×** | +7.1 | 1e-10 | 3/9 (HOP62, CFPAC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.92×** | +7.0 | 1e-10 | 7/15 (NCI-H460, HEC-1-A, …) | all doses, flat | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +7.0 | 1e-10 | 24/38 (A498, SW1417, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +5.9 | 2e-07 | 22/47 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.60×** | +5.3 | 6e-06 | 11/29 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.59×** | +5.2 | 9e-06 | 15/38 (A498, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.9 | 4e-05 | 11/36 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.8 | 5e-05 | 11/47 (A498, HEC-1-A, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.7 | 1e-04 | 12/39 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.05 µM |  | **1.47×** | +4.2 | 0.001 | 10/40 (HCT15, H4, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.004 | 8/47 (A498, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +3.7 | 0.005 | 12/43 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.037 | 7/42 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.066 | 3/43 (NCI-H460, SNU-423, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +2.8 | 0.096 | 5/44 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14426.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Phenytoin (sodium) (drug)]] 0.05 µM in 1 line (KATO III 0.0523×); [[Rosiglitazone (drug)]] 5 µM in 1 line (NCI-H1573 0.0735×); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0693×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.870× | -5.6 | 1e-05 | 24/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 5.44 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 19.0× (z +14.9) | — |
| [[NCI-H1573 (line)]] | alt | 4.76 | 0 | 2 (1 ⚠) | — | [[Rosiglitazone (drug)]] 5 µM 0.0735× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 4.15 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.111× (z -8.9) |
| [[A-172 (line)]] | wt | 4.93 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0948× (z -9.1) |
| [[A-427 (line)]] | wt | 5.21 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.1× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 4.72 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.113× (z -8.8) |
| [[Hs 766T (line)]] | wt | 6.02 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.102× (z -8.7) |
| [[KATO III (line)]] | alt | 7.44 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0523× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 5.11 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0693× (z -9.4) |
| [[PANC-1 (line)]] | alt | 3.71 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.47× (z +9.2) | — |
| [[A549 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETFBKMT]] | +0.64 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[ATP6V1C2]] | +0.62 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SMPD3]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SYN3]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[VCAN-AS1]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 | same gene group |
| [[PRKCA-AS1]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 | same gene group |
| [[CNTNAP5]] | +0.60 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CCDC39]] | +0.59 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[AKAP13-AS1]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 | same gene group |
| [[USH2A]] | +0.59 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[CNTN5]] | +0.58 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.57 | +0.49 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | -0.50 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[PROSER1]] | -0.49 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[TSEN15]] | -0.48 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[ZC3HAV1L]] | -0.47 | -0.37 / -0.53 | both halves | 9e-05 |  |
| [[CEP20]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMBP]] | B | AMBP activity raises CYP2U1-AS1's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.19× lower at baseline in the lines without AMBP | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[PMEL]] | B | PMEL activity raises CYP2U1-AS1's level | lines that do not express PMEL (13) vs lines expressing it (37) | 1.25× lower at baseline in the lines without PMEL | 0.032 | ⚠ within organs, on part of the lines; also absent: CGN, SH3BGRL2, MDFI; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CYP2U1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.1, 33.4); signed map (28.7, 17.7). **Vector** length 43.6, 4.55% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +5.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +5.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +4.9 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +3.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | -0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -5.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -0.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | CYP2U1 and SGMS2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q25 — chr4:107,863,473-107,989,724 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54817) · Entrez [101929595](https://www.ncbi.nlm.nih.gov/gene/101929595) · Ensembl [ENSG00000245293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245293)

## Data

Gene col 14426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14426); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14426]; `tensor/DDL_lfc|DDL_z.npy` [14426]; `embed/gene_vectors.npy` [14426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14426 or target_col == 14426). Every well: [[CYP2U1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP2U1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
