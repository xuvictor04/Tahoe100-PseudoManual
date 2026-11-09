---
symbol: "ZSCAN31"
type: "gene"
col: 14000
ensembl_id: "ENSG00000235109"
name: "zinc finger and SCAN domain containing 31"
location: "6p22.1"
module: 117
arm: "+"
pooled_cpm: 6.32
n_lines_expressing: 42
n_dd_up: 47
n_dd_down: 8
n_dd_up_clean: 41
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# ZSCAN31

*zinc finger and SCAN domain containing 31* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.80× (z +12.7, q 3e-34, up in 23 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.612× (z -4.3, q 0.004, down in 15 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRP1B]] (+0.69, fdr 9e-06), [[CAPS2]] (+0.67, fdr 7e-06), [[TRIM16L]] (+0.67, fdr 7e-06); moves opposite to [[RASA2]] (-0.61, fdr 1e-05), [[NIBAN2]] (-0.57, fdr 2e-05), [[HMGA2]] (-0.57, fdr 1e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AKR1C1]] → it (grade B ⚠); 2 go from it, the strongest it → [[NXPH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.80×** | +12.7 | 3e-34 | 23/31 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.26×** | +12.7 | 3e-34 | 28/34 (PANC-1, LS 180, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.62×** | +8.1 | 1e-13 | 26/34 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.46×** | +7.9 | 5e-13 | 19/30 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.17×** | +6.5 | 1e-08 | 21/35 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.16×** | +6.5 | 1e-08 | 15/34 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.82×** | +6.3 | 2e-08 | 24/36 (PANC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **2.06×** | +6.3 | 2e-08 | 23/37 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.79×** | +6.2 | 4e-08 | 22/36 (PANC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.67×** | +6.2 | 4e-08 | 24/37 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.86×** | +5.7 | 5e-07 | 20/40 (PANC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +5.6 | 1e-06 | 7/23 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.87×** | +5.5 | 2e-06 | 22/36 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.87×** | +5.4 | 2e-06 | 18/39 (PANC-1, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.74×** | +5.3 | 5e-06 | 19/39 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.2 | 7e-06 | 6/32 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14000.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.612×** | -4.3 | 0.004 | 15/37 (NCI-H460, SHP-77, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.615×** | -4.3 | 0.004 | 16/37 (COLO 205, SHP-77, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.429×** | -3.9 | 0.017 | 16/25 (COLO 205, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.649×** | -3.8 | 0.017 | 10/33 (NCI-H460, H4, …) | all doses, flat |  |
| [[Megestrol (drug)]] 5 µM |  | **0.741×** | -3.8 | 0.017 | 14/38 (NCI-H1573, H4, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.662×** | -3.5 | 0.035 | 11/38 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.673×** | -3.5 | 0.035 | 16/37 (NCI-H1573, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.695×** | -3.2 | 0.085 | 17/38 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.706× | -3.1 | 0.12 | 13/37 (NCI-H460, H4, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | 0.714× | -3.0 | 0.15 | 11/37 (Panc 03.27, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.84 | 10 | 0 | [[Auranofin (drug)]] 5 µM 9.79× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 26.3 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0980× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -9.0) |
| [[SHP-77 (line)]] | alt | 41.7 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 6.74× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -13.5) |
| [[H4 (line)]] | wt | 36.0 | 0 | 2 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0283× (z -11.0) ⚠ unreliable plate only · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0455× (z -9.7) |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0470× (z -9.0) ⚠ cell-cycle shift, explains ~76% of this change |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0275× (z -13.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 7.55 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.46× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.60 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 3.93× (z +15.2) ⚠ position not correctable | — |
| [[NCI-H23 (line)]] | alt | 4.42 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 3.76× (z +11.4) ⚠ position not correctable | — |
| [[SW480 (line)]] | alt | 2.37 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.114× (z -8.9) |
| [[A-172 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP1B]] | +0.69 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[CAPS2]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[TRIM16L]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[EGF]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ALOX12P2-1]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[IGSF1]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[EPHA5-AS1]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[GNGT1]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TLR6]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[TLR1]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[THSD7A]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[BBOX1-AS1]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASA2]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[NIBAN2]] | -0.57 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[HMGA2]] | -0.57 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[PKP2]] | -0.57 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[RECQL]] | -0.56 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[CAPRIN2]] | -0.56 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[PTPN12]] | -0.55 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[TBC1D8]] | -0.54 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ERI1]] | -0.54 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[ELK3]] | -0.53 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[DPY19L3]] | -0.53 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[SLCO4A1]] | -0.53 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C1]] | B | AKR1C1 activity raises ZSCAN31's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.94× lower at baseline in the lines without AKR1C1 | 0.057 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NXPH1]] | B | ZSCAN31 activity raises NXPH1's level | lines that do not express ZSCAN31 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without ZSCAN31 | 0.075 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[OSGIN1]] | B | ZSCAN31 activity raises OSGIN1's level | lines that do not express ZSCAN31 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without ZSCAN31 | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.5, 48.2); signed map (50.3, -8.5). **Vector** length 96.6, 22.8% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Synthesis of bile acids and bile salts via 27-hydroxycholesterol* (reactome, mean cos +0.51 to 3); *Synthesis of bile acids and bile salts via 24-hydroxycholesterol* (reactome, mean cos +0.51 to 3); *Synthesis of bile acids and bile salts via 7alpha-hydroxycholesterol* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.1 | +12.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.4 | +6.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.9 | +6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.8 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +12.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +5.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.6 | -4.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.5 | -4.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.1 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -2.9 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.7 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,324,693-28,356,271 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNF310P, ZNF323 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LW9](https://www.uniprot.org/uniprotkb/Q96LW9) (Zinc finger and SCAN domain-containing protein 31):

> May function as a transcription factor. May be involved in the development of multiple embryonic organs.

**Summary**, from NCBI Gene [64288](https://www.ncbi.nlm.nih.gov/gene/64288):

> This gene encodes a protein containing multiple C2H2-type zinc finger motifs. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:14097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14097) · Entrez [64288](https://www.ncbi.nlm.nih.gov/gene/64288) · UniProt [Q96LW9](https://www.uniprot.org/uniprotkb/Q96LW9) · Ensembl [ENSG00000235109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235109)

## Data

Gene col 14000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14000); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14000]; `tensor/DDL_lfc|DDL_z.npy` [14000]; `embed/gene_vectors.npy` [14000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14000 or target_col == 14000). Every well: [[ZSCAN31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
