---
symbol: "COPB2"
type: "gene"
col: 11535
ensembl_id: "ENSG00000184432"
name: "coat protein complex I subunit beta 2"
location: "3q23"
module: 56
arm: "+"
pooled_cpm: 182.29
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# COPB2

*coat protein complex I subunit beta 2* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +10.6, q 2e-23, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.749× (z -6.4, q 1e-07, down in 29 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 0.869× (z -4.6, q 0.001, down in 10 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPB1]] (+0.78, fdr 7e-06), [[SEC31A]] (+0.74, fdr 7e-06), [[GOLGA5]] (+0.74, fdr 7e-06); moves opposite to [[TET3]] (-0.57, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GALNT3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MON2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +10.6 | 2e-23 | 39/49 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +9.4 | 2e-18 | 42/49 (HS-578T, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +5.9 | 6e-07 | 30/48 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.8 | 2e-04 | 27/50 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.9 | 0.012 | 20/48 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.012 | 22/49 (A498, LOX-IMVI, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.7 | 0.016 | 23/45 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.042 | 18/44 (SNU-423, A498, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.4 | 0.042 | 11/49 (C32, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11535.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.749×** | -6.4 | 1e-07 | 29/47 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.869× | -4.6 | 0.001 | 10/48 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.820×** | -4.5 | 0.001 | 28/48 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.832×** | -4.2 | 0.003 | 23/48 (SW 1088, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.828×** | -4.2 | 0.003 | 23/48 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.820×** | -4.1 | 0.004 | 24/48 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.840× | -4.0 | 0.005 | 18/48 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.845× | -3.9 | 0.008 | 23/48 (A498, SW 900, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.846× | -3.4 | 0.032 | 20/48 (HEC-1-A, KATO III, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.846× | -3.4 | 0.032 | 21/49 (LoVo, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 284 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.359× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 268 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 159 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +10.8) | — |
| [[A498 (line)]] | wt | 184 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.23× (z +10.5) | — |
| [[A-427 (line)]] | wt | 166 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 192 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 294 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.58× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 89.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 202 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.64× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 130 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 184 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 244 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 170 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 198 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.17× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 141 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +17.6) | — |
| [[NCI-H2030 (line)]] | alt | 87.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 216 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 238 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 188 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +8.9) | — |
| [[SW 1088 (line)]] | alt | 238 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0368× (z -17.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 277 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +10.7) | — |
| [[A-172 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 152 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 174 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 153 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 357 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 209 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 198 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 172 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 213 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPB1]] | +0.78 | +0.82 / +0.80 | both halves | 7e-06 | same gene group; pathway: HALLMARK_PROTEIN_SECRETION; STRING 999 |
| [[SEC31A]] | +0.74 | +0.76 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_PROTEIN_SECRETION; STRING 637 |
| [[GOLGA5]] | +0.74 | +0.82 / +0.64 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 459 |
| [[SEC24D]] | +0.73 | +0.75 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 486 |
| [[COPA]] | +0.72 | +0.65 / +0.80 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 999 |
| [[COPG1]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 999 |
| [[SRP54]] | +0.72 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[SERP1]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PGM3]] | +0.70 | +0.74 / +0.65 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SLC39A7]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.68 | +0.74 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[TMED2]] | +0.68 | +0.66 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 675 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TET3]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT3]] | B | GALNT3 activity raises COPB2's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without GALNT3 | 0.053 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MON2]] | C | COPB2's natural level strengthens MON2's drug response | COPB2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.11; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, -35.6); signed map (-52.1, 12.0). **Vector** length 142, 46.1% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *COPII-mediated vesicle transport* (reactome, mean cos +0.62 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.53 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.65 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.2 | +10.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.0 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.4 | +3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -0.5 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +2.6 | +1.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | -1.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | -1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.8 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -6.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -4.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.2 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | coat protein complex I subunit beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:139,353,946-139,389,736 (-) |
| Ensembl biotype | protein_coding |
| Also known as | beta'-COP, betaprime-COP |
| Gene groups (HGNC) | WD repeat domain containing; Coat protein complex I |
| Hallmark sets | PROTEIN_SECRETION, GLYCOLYSIS |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P35606](https://www.uniprot.org/uniprotkb/P35606) (Coatomer subunit beta'):

> The coatomer is a cytosolic protein complex that binds to dilysine motifs and reversibly associates with Golgi non-clathrin-coated vesicles, which further mediate biosynthetic protein transport from the ER, via the Golgi up to the trans Golgi network. Coatomer complex is required for budding from Golgi membranes, and is essential for the retrograde Golgi-to-ER transport of dilysine-tagged proteins. In mammals, the coatomer can only be recruited by membranes associated to ADP-ribosylation …

**Summary**, from NCBI Gene [9276](https://www.ncbi.nlm.nih.gov/gene/9276):

> The Golgi coatomer complex (see MIM 601924) constitutes the coat of nonclathrin-coated vesicles and is essential for Golgi budding and vesicular trafficking. It consists of 7 protein subunits, including COPB2.[supplied by OMIM, Jul 2002]

**Accessions** — [HGNC:2232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2232) · Entrez [9276](https://www.ncbi.nlm.nih.gov/gene/9276) · UniProt [P35606](https://www.uniprot.org/uniprotkb/P35606) · Ensembl [ENSG00000184432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184432)

## Data

Gene col 11535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11535); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11535]; `tensor/DDL_lfc|DDL_z.npy` [11535]; `embed/gene_vectors.npy` [11535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11535 or target_col == 11535). Every well: [[COPB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
