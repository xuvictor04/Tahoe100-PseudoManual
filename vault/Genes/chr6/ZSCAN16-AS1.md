---
symbol: "ZSCAN16-AS1"
type: "gene"
col: 15618
ensembl_id: "ENSG00000269293"
name: "ZSCAN16 antisense RNA 1"
location: "6p22.1"
module: 23
arm: "+"
pooled_cpm: 16.74
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ZSCAN16-AS1

*ZSCAN16 antisense RNA 1* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.63× (z +21.6, q 0e+00, up in 35 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.128×, RPMI-7951 0.112×, A-172 0.204×, SW 900 0.190×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (HCT15 0.0845×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.141×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.230×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF226]] (+0.68, fdr 9e-06), [[HCG27]] (+0.66, fdr 8e-06), [[VPS13B-DT]] (+0.66, fdr 7e-06); moves opposite to [[RGS19]] (-0.64, fdr 4e-05), [[TTLL12]] (-0.57, fdr 5e-05), [[SPTLC2]] (-0.55, fdr 5e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF790]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Fluvoxamine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.63×** | +21.6 | 0e+00 | 35/46 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +13.3 | 1e-37 | 37/47 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +9.4 | 7e-19 | 31/46 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +7.9 | 3e-13 | 27/47 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +7.7 | 1e-12 | 31/44 (HepG2/C3A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.4 | 9e-12 | 32/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +6.2 | 4e-08 | 23/46 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +5.2 | 1e-05 | 17/33 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.2 | 2e-05 | 22/47 (NCI-H2347, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +4.5 | 3e-04 | 17/47 (HOP62, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.3 | 8e-04 | 13/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 13/47 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 18/47 (SW480, HT-29, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.9 | 0.003 | 7/27 (SW480, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.004 | 14/46 (RKO, A-172, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.004 | 10/47 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.018 | 7/46 (LoVo, C32, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.019 | 5/47 (J82, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15618.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.128×, RPMI-7951 0.112×, A-172 0.204×, SW 900 0.190×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (HCT15 0.0845×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.141×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.230×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.784× | -3.7 | 0.13 | 17/46 (HepG2/C3A, SHP-77, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Peretinoin (drug)]] 5 µM |  | 0.806× | -3.3 | 0.30 | 8/46 (SW48, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 19.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.6) | — |
| [[A-172 (line)]] | wt | 17.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 15.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +10.7) | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0845× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 29.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +14.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.221× (z -9.2) ⚠ toxic |
| [[HOP62 (line)]] | alt | 32.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 20.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 29.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.112× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 9.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -9.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +18.4) | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.141× (z -9.9) |
| [[J82 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.1) | — |
| [[LoVo (line)]] | wt | 6.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +13.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 5.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +14.4) | — |
| [[NCI-H23 (line)]] | alt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 22.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF226]] | +0.68 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[HCG27]] | +0.66 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[VPS13B-DT]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ZNF506]] | +0.65 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[NAA38]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[LINC00938]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[HAVCR2]] | +0.64 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[TMEM80]] | +0.63 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[PNISR]] | +0.63 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CDKL3]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[THAP6]] | +0.63 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[LINC01772]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS19]] | -0.64 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[TTLL12]] | -0.57 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[SPTLC2]] | -0.55 | -0.66 / -0.24 | both halves | 5e-04 |  |
| [[TRAPPC9]] | -0.53 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[HSPA8]] | -0.52 | -0.61 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF790]] | B | ZNF790 activity raises ZSCAN16-AS1's level | lines that do not express ZNF790 (14) vs lines expressing it (36) | 1.56× lower at baseline in the lines without ZNF790 | 0.055 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF606, ZNF569 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | ZSCAN16-AS1's natural level raises the cells' numbers under Fluvoxamine 0.5 µM (protects the cells) | ZSCAN16-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.494 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-8.0, 27.7); signed map (25.7, -13.4). **Vector** length 87.2, 18.0% of its response variance represented; |z| ≥ 3 in 739 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +21.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.6 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +13.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +9.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +3.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.1 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.8 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ZSCAN16 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p22.1 — chr6:28,015,122-28,137,313 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100129195](https://www.ncbi.nlm.nih.gov/gene/100129195):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:48982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48982) · Entrez [100129195](https://www.ncbi.nlm.nih.gov/gene/100129195) · Ensembl [ENSG00000269293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269293)

## Data

Gene col 15618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15618); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15618]; `tensor/DDL_lfc|DDL_z.npy` [15618]; `embed/gene_vectors.npy` [15618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15618 or target_col == 15618). Every well: [[ZSCAN16-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN16-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
