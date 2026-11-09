---
symbol: "SAR1A"
type: "gene"
col: 1251
ensembl_id: "ENSG00000079332"
name: "secretion associated Ras related GTPase 1A"
location: "10q22.1"
module: 42
arm: "+"
pooled_cpm: 141.45
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SAR1A

*secretion associated Ras related GTPase 1A* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.45× (z +7.5, q 4e-11, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.703× (z -6.9, q 3e-09, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPA]] (+0.81, fdr 7e-06), [[DDB1]] (+0.76, fdr 7e-06), [[GGCX]] (+0.75, fdr 7e-06); moves opposite to [[CMTR2]] (-0.64, fdr 7e-06), [[RPP38]] (-0.60, fdr 7e-06), [[GCFC2]] (-0.60, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PAPSS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1251.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +7.5 | 4e-11 | 34/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.42×** | +7.0 | 7e-10 | 34/48 (SW480, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.33×** | +5.8 | 1e-06 | 32/48 (SW480, C-33 A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +5.7 | 1e-06 | 34/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.71×** | +5.7 | 2e-06 | 35/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.6 | 2e-06 | 33/48 (SW480, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +5.4 | 6e-06 | 37/45 (PANC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.30×** | +5.2 | 2e-05 | 29/48 (SW480, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.20×** | +5.2 | 2e-05 | 24/49 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.25×** | +4.5 | 5e-04 | 25/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.25×** | +4.4 | 6e-04 | 27/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.24×** | +4.2 | 0.001 | 25/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.9 | 0.004 | 22/38 (PANC-1, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.005 | 23/48 (hTERT-HPNE, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1251.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.703×** | -6.9 | 3e-09 | 33/48 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.822×** | -5.6 | 5e-06 | 26/48 (NCI-H2347, A498, …) | inconsistent across doses | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.762×** | -5.3 | 2e-05 | 31/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -4.4 | 0.001 | 24/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.824×** | -3.8 | 0.019 | 23/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.836× | -3.7 | 0.023 | 21/48 (A549, SNU-423, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.886× | -3.5 | 0.036 | 7/48 (NCI-H661, NCI-H460, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.846× | -3.4 | 0.046 | 17/48 (Hs 766T, RPMI-7951, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.853× | -3.2 | 0.073 | 16/49 (SW1417, LS 180, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 228 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +21.0) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +16.0) | — |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -19.1) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.432× (z -12.4) |
| [[A498 (line)]] | wt | 211 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.461× (z -13.1) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.521× (z -10.6) |
| [[SW480 (line)]] | alt | 122 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +12.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 126 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +12.5) | — |
| [[KATO III (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -9.5) ⚠ cell-cycle shift, explains ~4% of this change |
| [[LoVo (line)]] | wt | 145 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.456× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 95.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SHP-77 (line)]] | alt | 48.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 84.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 147 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 204 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 206 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 123 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 177 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 101 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 121 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPA]] | +0.81 | +0.85 / +0.76 | both halves | 7e-06 | STRING 451 |
| [[DDB1]] | +0.76 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[GGCX]] | +0.75 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.75 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[SURF4]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 | STRING 756 |
| [[SEC24C]] | +0.73 | +0.78 / +0.63 | both halves | 7e-06 | same gene group; STRING 992 |
| [[NDEL1]] | +0.72 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.72 | +0.77 / +0.68 | both halves | 7e-06 | same gene group; STRING 987 |
| [[DERL1]] | +0.71 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[TM9SF2]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[P3H1]] | +0.70 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMTR2]] | -0.64 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[RPP38]] | -0.60 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[GCFC2]] | -0.60 | -0.71 / -0.46 | both halves | 2e-05 |  |
| [[URGCP]] | -0.60 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[DCUN1D1]] | -0.59 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ITSN2]] | -0.59 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.59 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[STAT5B]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[NT5C]] | -0.59 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[ZC3H7B]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPSS2]] | B | PAPSS2 activity raises SAR1A's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 1.17× lower at baseline in the lines without PAPSS2 | 0.071 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[HOXA7]] | B | HOXA7 activity raises SAR1A's level | lines that do not express HOXA7 (26) vs lines expressing it (24) | 1.14× lower at baseline in the lines without HOXA7 | 0.095 | ⚠ within organs, on part of the lines; also absent: NKD1, GRIN2B, LINC02253 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, -30.9); signed map (-52.8, 6.8). **Vector** length 124, 38.1% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.63 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.59 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.59 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.2 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +1.8 | +2.6 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +1.6 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.6 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -10.0 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -7.3 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -4.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.4 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -5.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.7 | -3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | secretion associated Ras related GTPase 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:70,147,289-70,170,523 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAR1, Sara; previously SARA1 |
| Gene groups (HGNC) | ARF GTPase family; Coat protein complex II |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR31](https://www.uniprot.org/uniprotkb/Q9NR31) (Small COPII coat GTPase SAR1A):

> Small GTPase that cycles between an active GTP-bound and an inactive GDP-bound state and mainly functions in vesicle-mediated endoplasmic reticulum (ER) to Golgi transport. The active GTP-bound form inserts into the endoplasmic reticulum membrane where it recruits the remainder of the coat protein complex II/COPII. The coat protein complex II assembling and polymerizing on endoplasmic reticulum membrane is responsible for both the sorting of cargos and the deformation and budding of membranes …

**Summary**, from NCBI Gene [56681](https://www.ncbi.nlm.nih.gov/gene/56681):

> Enables G protein activity and amino acid sensor activity. Involved in COPII-coated vesicle budding; cellular response to leucine starvation; and negative regulation of TORC1 signaling. Located in endoplasmic reticulum. Is active in COPII vesicle coat; endoplasmic reticulum exit site; and lysosomal membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10534](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10534) · Entrez [56681](https://www.ncbi.nlm.nih.gov/gene/56681) · UniProt [Q9NR31](https://www.uniprot.org/uniprotkb/Q9NR31) · Ensembl [ENSG00000079332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079332)

## Data

Gene col 1251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1251); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1251]; `tensor/DDL_lfc|DDL_z.npy` [1251]; `embed/gene_vectors.npy` [1251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1251 or target_col == 1251). Every well: [[SAR1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAR1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
