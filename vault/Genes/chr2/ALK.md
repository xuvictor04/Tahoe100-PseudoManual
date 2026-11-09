---
symbol: "ALK"
type: "gene"
col: 10047
ensembl_id: "ENSG00000171094"
name: "ALK receptor tyrosine kinase"
location: "2p23.2-p23.1"
module: 61
arm: "+"
pooled_cpm: 9.3
n_lines_expressing: 43
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# ALK

*ALK receptor tyrosine kinase* — 2p23.2-p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.75× (z +23.6, q 0e+00, up in 27 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.685× (z -4.7, q 0.001, down in 17 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYN3]] (+0.72, fdr 7e-06), [[MTUS2]] (+0.66, fdr 2e-05), [[DLGAP2]] (+0.65, fdr 1e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HTR7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.75×** | +23.6 | 0e+00 | 27/35 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.30×** | +18.4 | 0e+00 | 33/40 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.80×** | +18.4 | 0e+00 | 35/40 (A-427, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.62×** | +16.3 | 0e+00 | 27/37 (HEC-1-A, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.37×** | +15.4 | 0e+00 | 28/39 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +13.3 | 2e-38 | 24/35 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +11.9 | 1e-30 | 13/26 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.34×** | +10.8 | 3e-25 | 27/40 (NCI-H23, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.30×** | +10.5 | 4e-24 | 24/38 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +9.6 | 4e-20 | 5/12 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +8.7 | 3e-16 | 21/37 (A-427, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +7.9 | 1e-13 | 25/40 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +7.1 | 5e-11 | 6/16 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.7 | 9e-10 | 14/40 (NCI-H460, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +6.7 | 1e-09 | 12/35 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.9 | 1e-07 | 12/35 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.008 | 8/36 (NCI-H1573, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.050 | 10/33 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10047.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.685×** | -4.7 | 0.001 | 17/41 (HS-578T, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.731×** | -3.9 | 0.019 | 13/37 (H4, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.733×** | -3.9 | 0.019 | 9/35 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.755×** | -3.5 | 0.066 | 10/40 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Vilanterol (drug)]] 5 µM |  | 0.831× | -3.2 | 0.13 | 6/39 (SW 1271, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.39 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 43.2× (z +18.7) | — |
| [[C32 (line)]] | wt | 78.3 | 0 | 5 (3 ⚠) | — | [[Radotinib (drug)]] 5 µM 0.221× (z -10.3) |
| [[A-427 (line)]] | wt | 3.69 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 15.2× (z +11.8) | — |
| [[A498 (line)]] | wt | 3.97 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 24.9× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 3.73 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 52.7× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 20.7× (z +12.7) | — |
| [[SW480 (line)]] | alt | 52.3 | 0 | 4 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.199× (z -11.1) ⚠ transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.402× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 9.38 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 16.7× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 2.55 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 21.1× (z +11.9) | — |
| [[A549 (line)]] | wt | 5.22 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +11.2) | — |
| [[H4 (line)]] | wt | 24.4 | 0 | 2 (2 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0628× (z -9.0) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 21.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0455× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[SW 1088 (line)]] | alt | 208 | 0 | 2 (1 ⚠) | — | [[Budesonide (drug)]] 0.05 µM 0.0362× (z -9.6) |
| [[SW 900 (line)]] | alt | 11.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 13.1× (z +9.6) | — |
| [[A-172 (line)]] | wt | 8.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 14.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.10× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 3.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.23× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 3.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.35× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 8.61 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.0698× (z -9.4) |
| [[SHP-77 (line)]] | alt | 6.15 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.42× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.89× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 3.42 | 0 | 1 | — | [[Hydroxyurea (drug)]] 5 µM 0.0600× (z -9.1) |
| [[AN3 CA (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYN3]] | +0.72 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[MTUS2]] | +0.66 | +0.48 / +0.72 | both halves | 2e-05 | STRING 704 |
| [[DLGAP2]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[SYN1]] | +0.64 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[COL23A1]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[VAT1L]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SORCS1]] | +0.62 | +0.46 / +0.72 | both halves | 3e-05 |  |
| [[ZMAT4]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[HS6ST3]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ATP8A2]] | +0.61 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[DACH2]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ALK's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TDRD9]] | B | TDRD9 activity raises ALK's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 2.14× lower at baseline in the lines without TDRD9 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises ALK's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.51× lower at baseline in the lines without FKBP9P1-1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[LEF1-AS1]] | B | LEF1-AS1 activity raises ALK's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 2.60× lower at baseline in the lines without LEF1-AS1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| [[VAT1L]] | B | VAT1L activity raises ALK's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without VAT1L | 0.064 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent |
| [[TNC]] | B | TNC activity raises ALK's level | lines that do not express TNC (23) vs lines expressing it (27) | 2.37× lower at baseline in the lines without TNC | 0.089 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTR7]] | B | ALK activity raises HTR7's level | lines that do not express ALK (7) vs lines expressing it (43) | 3.38× lower at baseline in the lines without ALK | 0.086 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, BBS5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.4, 32.7); signed map (30.0, 17.8). **Vector** length 85.4, 17.1% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.3 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.1 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.0 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.2 | +16.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +6.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.3 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ALK receptor tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.2-p23.1 — chr2:29,192,774-29,921,586 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD246, ALK1 |
| Gene groups (HGNC) | CD molecules; ALK and LTK receptor tyrosine kinase family |
| Reactome | 7 pathways, smallest: MDK and PTN in ALK signaling; ALK mutants bind TKIs; Signaling by ALK |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM73](https://www.uniprot.org/uniprotkb/Q9UM73) (ALK tyrosine kinase receptor):

> Neuronal receptor tyrosine kinase that is essentially and transiently expressed in specific regions of the central and peripheral nervous systems and plays an important role in the genesis and differentiation of the nervous system. Also acts as a key thinness protein involved in the resistance to weight gain: in hypothalamic neurons, controls energy expenditure acting as a negative regulator of white adipose tissue lipolysis and sympathetic tone to fine-tune energy homeostasis (By similarity). …

**Summary**, from NCBI Gene [238](https://www.ncbi.nlm.nih.gov/gene/238):

> This gene encodes a receptor tyrosine kinase, which belongs to the insulin receptor superfamily. This protein comprises an extracellular domain, an hydrophobic stretch corresponding to a single pass transmembrane region, and an intracellular kinase domain. It plays an important role in the development of the brain and exerts its effects on specific neurons in the nervous system. This gene has been found to be rearranged, mutated, or amplified in a series of tumours including anaplastic large …

**Accessions** — [HGNC:427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:427) · Entrez [238](https://www.ncbi.nlm.nih.gov/gene/238) · UniProt [Q9UM73](https://www.uniprot.org/uniprotkb/Q9UM73) · Ensembl [ENSG00000171094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171094)

## Data

Gene col 10047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10047); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10047]; `tensor/DDL_lfc|DDL_z.npy` [10047]; `embed/gene_vectors.npy` [10047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10047 or target_col == 10047). Every well: [[ALK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
