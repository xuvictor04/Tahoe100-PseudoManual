---
symbol: "TPP1"
type: "gene"
col: 9287
ensembl_id: "ENSG00000166340"
name: "tripeptidyl peptidase 1"
location: "11p15.4"
module: 122
arm: "+"
pooled_cpm: 27.81
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# TPP1

*tripeptidyl peptidase 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.00× (z +14.9, q 0e+00, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.657× (z -6.2, q 3e-07, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNS]] (+0.82, fdr 7e-06), [[IGF2R]] (+0.74, fdr 7e-06), [[CTSA]] (+0.73, fdr 7e-06); moves opposite to [[MRPS26]] (-0.60, fdr 3e-05), [[POP7]] (-0.58, fdr 2e-05), [[FBXO45]] (-0.57, fdr 1e-04).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9287.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +14.9 | 0e+00 | 36/46 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +13.2 | 1e-37 | 30/32 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +13.0 | 1e-36 | 39/43 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +11.4 | 4e-28 | 29/36 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +8.4 | 4e-15 | 38/47 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.5 | 8e-12 | 30/46 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +7.2 | 7e-11 | 32/47 (LoVo, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +5.5 | 3e-06 | 27/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +5.4 | 4e-06 | 27/47 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.9 | 6e-05 | 22/44 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.5 | 4e-04 | 24/46 (HEC-1-A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 8e-04 | 19/46 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +4.3 | 8e-04 | 24/47 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.001 | 22/47 (A-172, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.002 | 20/47 (RKO, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 12/47 (NCI-H1573, A-172, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.30×** | +3.8 | 0.005 | 17/47 (NCI-H1573, A498, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.037 | 12/46 (SNU-1, SW48, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.053 | 10/46 (Hs 766T, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9287.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.657×** | -6.2 | 3e-07 | 34/46 (HepG2/C3A, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.671×** | -6.1 | 3e-07 | 34/47 (NCI-H661, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.734×** | -4.7 | 4e-04 | 25/47 (CFPAC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.769×** | -3.7 | 0.030 | 24/45 (A-172, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Allantoin (drug)]] 0.5 µM |  | **0.790×** | -3.6 | 0.035 | 18/46 (Hs 766T, HCT15, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **0.729×** | -3.4 | 0.053 | 14/46 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.864× | -3.2 | 0.11 | 16/47 (SW480, LS 180, …) | top dose only | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 0.864× | -3.2 | 0.11 | 10/47 (SNU-1, CFPAC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 40.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.37× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +17.8) | — |
| [[A498 (line)]] | wt | 18.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 35.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +13.2) | — |
| [[HEC-1-A (line)]] | alt | 14.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.61× (z +8.8) | — |
| [[J82 (line)]] | alt | 74.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +19.6) | — |
| [[A-172 (line)]] | wt | 43.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +20.5) | — |
| [[HepG2_C3A (line)]] | wt | 33.4 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.171× (z -11.3) |
| [[Hs 766T (line)]] | wt | 43.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +22.3) | — |
| [[HT-29 (line)]] | alt | 32.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.3) | — |
| [[LoVo (line)]] | wt | 15.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.54× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 27.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 26.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +16.7) | — |
| [[A-427 (line)]] | wt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0978× (z -12.4) |
| [[COLO 205 (line)]] | alt | 33.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +11.0) | — |
| [[KATO III (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 28.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.9) | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 1 | — | [[Everolimus (drug)]] 0.05 µM 0.112× (z -9.3) |
| [[SNU-423 (line)]] | alt | 78.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +15.8) | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNS]] | +0.82 | +0.80 / +0.80 | both halves | 7e-06 | STRING 622 |
| [[IGF2R]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CTSA]] | +0.73 | +0.68 / +0.74 | both halves | 7e-06 | STRING 623 |
| [[GBA1]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[ATP6AP1]] | +0.70 | +0.63 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ATP6V1C1]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[LAMP1]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 | STRING 401 |
| [[BAG6]] | +0.67 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[VPS11]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[LAMP2]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[DVL2]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[LAMTOR3]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS26]] | -0.60 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[POP7]] | -0.58 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[FBXO45]] | -0.57 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[SAC3D1]] | -0.55 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[KIF2A]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[GADD45GIP1]] | -0.52 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[MTLN]] ⚠ | -0.52 | -0.30 / -0.53 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS34]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[BRIX1]] | -0.50 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[SNU13]] | -0.50 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[TOMM5]] | -0.49 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[PET117]] | -0.49 | -0.29 / -0.46 | both halves | 3e-04 |  |
| [[LSM2]] | -0.48 | -0.35 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TPP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.741). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-21.7, -20.5); signed map (-24.1, -35.9). **Vector** length 105, 24.9% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +14.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +7.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.2 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -6.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | tripeptidyl peptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,612,768-6,619,448 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LPIC, TPP-1; previously CLN2, SCAR7 |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [O14773](https://www.uniprot.org/uniprotkb/O14773) (Tripeptidyl-peptidase 1):

> Lysosomal serine protease with tripeptidyl-peptidase I activity. May act as a non-specific lysosomal peptidase which generates tripeptides from the breakdown products produced by lysosomal proteinases. Requires substrates with an unsubstituted N-terminus.

**Summary**, from NCBI Gene [1200](https://www.ncbi.nlm.nih.gov/gene/1200):

> This gene encodes a member of the sedolisin family of serine proteases. The protease functions in the lysosome to cleave N-terminal tripeptides from substrates, and has weaker endopeptidase activity. It is synthesized as a catalytically-inactive enzyme which is activated and auto-proteolyzed upon acidification. Mutations in this gene result in late-infantile neuronal ceroid lipofuscinosis, which is associated with the failure to degrade specific neuropeptides and a subunit of ATP synthase in …

**Accessions** — [HGNC:2073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2073) · Entrez [1200](https://www.ncbi.nlm.nih.gov/gene/1200) · UniProt [O14773](https://www.uniprot.org/uniprotkb/O14773) · Ensembl [ENSG00000166340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166340)

## Data

Gene col 9287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9287); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9287]; `tensor/DDL_lfc|DDL_z.npy` [9287]; `embed/gene_vectors.npy` [9287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9287 or target_col == 9287). Every well: [[TPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
