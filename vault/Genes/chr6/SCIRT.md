---
symbol: "SCIRT"
type: "gene"
col: 14147
ensembl_id: "ENSG00000237686"
name: "stem cell inhibitory RNA transcript"
location: "6p21.1"
module: 37
arm: "+"
pooled_cpm: 13.28
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# SCIRT

*stem cell inhibitory RNA transcript* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +8.6, q 4e-15, up in 28 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.376× (z -11.7, q 7e-29, down in 32 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.397× (z -11.0, q 7e-26, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PELO-AS1]] (+0.65, fdr 1e-05), [[PIWIL2]] (+0.63, fdr 7e-06), [[TMEM225B]] (+0.62, fdr 1e-05); moves opposite to [[GNPTAB]] (-0.59, fdr 1e-05), [[CROT]] (-0.50, fdr 1e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02036]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.6 | 4e-15 | 28/42 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +8.1 | 1e-13 | 24/43 (LoVo, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +6.2 | 1e-07 | 24/44 (A-172, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +6.1 | 1e-07 | 22/44 (hTERT-HPNE, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.0 | 7e-05 | 3/46 (NCI-H23, HCT15, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.028 | 14/46 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.063 | 16/43 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.069 | 11/46 (A-172, SW1417, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.069 | 11/45 (SW480, A549, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.11 | 12/45 (SHP-77, HOP62, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.12 | 4/44 (HS-578T, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14147.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.376×** | -11.7 | 7e-29 | 32/43 (BT-474, H4, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.397×** | -11.0 | 7e-26 | 37/45 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.489×** | -8.6 | 2e-15 | 34/46 (BT-474, H4, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.479×** | -8.5 | 4e-15 | 29/45 (H4, SW480, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.494×** | -8.3 | 2e-14 | 32/45 (BT-474, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.522×** | -7.5 | 7e-12 | 23/38 (A549, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.562×** | -6.5 | 6e-09 | 27/43 (HOP62, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -6.3 | 3e-08 | 29/45 (BT-474, H4, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.439×** | -5.1 | 2e-05 | 19/45 (KATO III, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.458×** | -4.9 | 6e-05 | 21/33 (SK-MEL-2, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.750×** | -4.9 | 6e-05 | 20/46 (SW480, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.658×** | -4.8 | 7e-05 | 20/38 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.516×** | -4.1 | 0.001 | 17/41 (J82, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.721×** | -3.8 | 0.005 | 19/44 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.544×** | -3.8 | 0.005 | 14/40 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.753×** | -3.2 | 0.041 | 9/46 (HS-578T, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.765×** | -3.2 | 0.046 | 15/45 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.757×** | -3.1 | 0.057 | 12/44 (H4, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 57.3 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0385× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.141× (z -15.4) |
| [[H4 (line)]] | wt | 37.9 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0236× (z -18.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.147× (z -9.3) |
| [[SW480 (line)]] | alt | 13.6 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.395× (z -9.5) |
| [[HCT15 (line)]] | alt | 29.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.159× (z -9.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 24.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.125× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 25.8 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.195× (z -10.5) |
| [[KATO III (line)]] | alt | 19.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.154× (z -11.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[PANC-1 (line)]] | alt | 6.51 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.194× (z -9.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.187× (z -8.7) |
| [[SNU-423 (line)]] | alt | 36.7 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.169× (z -11.1) |
| [[A-172 (line)]] | wt | 8.98 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.121× (z -8.6) |
| [[A549 (line)]] | wt | 9.94 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0715× (z -11.8) ⚠ toxic |
| [[C32 (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 5.22 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0670× (z -9.1) ⚠ toxic |
| [[HS-578T (line)]] | alt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +10.3) | — |
| [[LoVo (line)]] | wt | 8.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +14.7) | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 3.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PELO-AS1]] | +0.65 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[PIWIL2]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TMEM225B]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[TMEM269]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[LNP1]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CHRNE]] | +0.60 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[DNAH10]] | +0.59 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[AMZ1]] | +0.59 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[LINC01422]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[EPHA1-AS1]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNPTAB]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[CROT]] | -0.50 | -0.47 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02036]] | B | LINC02036 activity raises SCIRT's level | lines that do not express LINC02036 (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without LINC02036 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00887, ENSG00000256982, SIPA1L2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, -16.5); signed map (12.4, 5.0). **Vector** length 90.3, 19.7% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.7 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.7 | +0.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -11.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.3 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.8 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.6 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -8.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -2.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.9 | -3.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | stem cell inhibitory RNA transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p21.1 — chr6:43,931,572-44,074,655 (-) |
| Ensembl biotype | lncRNA |
| Also known as | DATOC-1, AL109615.3 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55341) · Entrez [101929705](https://www.ncbi.nlm.nih.gov/gene/101929705) · Ensembl [ENSG00000237686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237686)

## Data

Gene col 14147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14147); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14147]; `tensor/DDL_lfc|DDL_z.npy` [14147]; `embed/gene_vectors.npy` [14147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14147 or target_col == 14147). Every well: [[SCIRT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCIRT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
