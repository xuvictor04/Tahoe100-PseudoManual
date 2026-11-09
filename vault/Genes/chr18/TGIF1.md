---
symbol: "TGIF1"
type: "gene"
col: 10821
ensembl_id: "ENSG00000177426"
name: "TGFB induced factor homeobox 1"
location: "18p11.31"
module: 95
arm: "+"
pooled_cpm: 50.72
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/095", "written"]
generated_by: "tahoemap"
---

# TGIF1

*TGFB induced factor homeobox 1* — 18p11.31

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> TGIF1 is a TALE-class homeodomain repressor that caps the output of TGF-beta and Nodal signalling by binding activated Smad2 and recruiting corepressors.

## What it is

TGIF1 is a TALE-class homeodomain protein, kin to PBX and MEIS, and acts almost entirely as a repressor. It was first described blocking RXR-dependent transcription at a retinoid-responsive element, but its characterised role is in TGF-beta signalling: TGIF1 binds activated Smad2 in the nucleus and turns the Smad complex into a repressor by recruiting mSin3/HDAC and CtBP. Because TGIF1 is itself TGF-beta-inducible, it is a feedback node rather than a constitutive brake. Heterozygous mutations and 18p deletions cause holoprosencephaly, and the disease alleles hit the DNA-binding surface, the repression domain, or the Smad2-interaction region — much of the evidence that the Smad role is the physiologically important one.

## What is uncertain

TGIF1's curated target set is small, so an activity inferred from it is close to an average over a handful of transcripts. The deeper problem is directional: TGIF1 represses, while the activity convention reads coordinated target expression as factor activity, so the sign cannot be taken at face value. The regulon is also inseparable from Smad-driven transcription, since TGIF1 is TGF-beta-induced and acts on Smad targets — the score may report pathway tone rather than TGIF1 itself.

## References

- Wotton et al., 1999, Cell — identified TGIF as a Smad2-binding transcriptional corepressor of TGF-beta signalling.
- Melhuish & Wotton, 2000, Journal of Biological Chemistry — showed TGIF recruits CtBP, and that a holoprosencephaly mutation disrupts that interaction.
- Gripp et al., 2000, Nature Genetics — heterozygous TGIF mutations cause holoprosencephaly, linking Nodal signalling to human neural axis determination.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.87× (z +14.8, q 0e+00, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.243× (z -29.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB2]] (+0.55, fdr 3e-05), [[DLGAP1-AS1]] (+0.53, fdr 1e-05), [[FOSL2]] (+0.53, fdr 2e-05); moves opposite to [[DIP2A]] (-0.49, fdr 1e-04), [[PPM1F]] (-0.46, fdr 4e-04), [[DGKZ]] (-0.45, fdr 2e-04).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BATF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.87×** | +14.8 | 0e+00 | 44/49 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +7.0 | 6e-10 | 30/48 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +5.3 | 2e-05 | 23/46 (A-172, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +4.0 | 0.009 | 19/47 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.017 | 15/47 (LS 180, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.017 | 21/47 (HOP62, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.19× | +3.7 | 0.017 | 18/48 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.19× | +3.5 | 0.029 | 16/47 (LOX-IMVI, HT-29, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.16× | +3.1 | 0.12 | 9/48 (C-33 A, A498, …) | inconsistent across doses |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.12 | 7/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.16× | +3.0 | 0.12 | 7/48 (HT-29, Hs 766T, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10821.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.243×** | -29.6 | 0e+00 | 48/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.264×** | -27.8 | 0e+00 | 47/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.447×** | -16.8 | 0e+00 | 44/48 (LS 180, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.494×** | -14.1 | 3e-43 | 32/41 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.606×** | -10.1 | 8e-22 | 40/44 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -8.5 | 2e-15 | 35/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.669×** | -8.1 | 6e-14 | 33/47 (A-427, NCI-H23, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **0.685×** | -7.9 | 2e-13 | 29/47 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.523×** | -7.1 | 9e-11 | 31/48 (A-427, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.548×** | -6.6 | 3e-09 | 28/48 (NCI-H23, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.565×** | -6.2 | 2e-08 | 30/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.583×** | -5.9 | 2e-07 | 25/47 (LS 180, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.788×** | -5.0 | 3e-05 | 21/48 (SW480, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.789×** | -4.9 | 3e-05 | 25/48 (SW480, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.790×** | -4.9 | 3e-05 | 24/48 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.639×** | -4.9 | 4e-05 | 17/48 (NCI-H23, A498, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.808×** | -4.4 | 3e-04 | 20/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **0.814×** | -4.1 | 0.001 | 14/48 (HepG2/C3A, Panc 03.27, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.721×** | -3.6 | 0.009 | 15/47 (H4, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.733×** | -3.4 | 0.017 | 9/48 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.893× | -3.4 | 0.019 | 14/48 (SNU-1, C32, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.858× | -3.2 | 0.031 | 10/48 (RPMI-7951, LoVo, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.860× | -3.1 | 0.036 | 18/48 (SW48, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 82.3 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -24.8) |
| [[NCI-H460 (line)]] | wt | 96.0 | 4 (3 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.96× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.170× (z -18.8) |
| [[NCI-H1573 (line)]] | alt | 71.5 | 1 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 14.4× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.130× (z -20.3) |
| [[LoVo (line)]] | wt | 62.0 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 124 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.208× (z -14.4) |
| [[A-427 (line)]] | wt | 121 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.92× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.235× (z -16.1) |
| [[KATO III (line)]] | alt | 59.1 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -17.5) |
| [[C-33 A (line)]] | alt | 59.8 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.51× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.159× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 40.9 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -14.4) |
| [[SW48 (line)]] | wt | 68.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.138× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 22.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Panobinostat (drug)]] 5 µM 0.258× (z -11.3) |
| [[HT-29 (line)]] | alt | 58.1 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 49.2 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -12.0) |
| [[PANC-1 (line)]] | alt | 64.0 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -19.0) |
| [[SNU-423 (line)]] | alt | 52.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -10.9) |
| [[SW480 (line)]] | alt | 50.2 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -17.9) |
| [[A498 (line)]] | wt | 30.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -11.7) |
| [[A549 (line)]] | wt | 50.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -14.5) |
| [[COLO 205 (line)]] | alt | 49.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 51.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -12.5) |
| [[Hs 766T (line)]] | wt | 38.0 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 10.9× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.198× (z -11.5) |
| [[SW1417 (line)]] | alt | 44.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -11.7) |
| [[A-172 (line)]] | wt | 36.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -11.0) |
| [[HOP62 (line)]] | alt | 54.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.385× (z -8.5) |
| [[HS-578T (line)]] | alt | 37.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -12.3) |
| [[J82 (line)]] | alt | 40.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 27.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 38.9 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 9.87× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.299× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 37.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 39.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -10.6) |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0793× (z -18.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 35.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -12.0) |
| [[C32 (line)]] | wt | 40.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 24.1× (z +12.2) | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.299× (z -9.2) |
| [[H4 (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[MIA PaCa-2 (line)]] | alt | 56.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.382× (z -8.8) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 23.5 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.207× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 37.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -10.5) |
| [[SNU-1 (line)]] | wt | 86.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB2]] | +0.55 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[DLGAP1-AS1]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[FOSL2]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GAPLINC]] | +0.51 | +0.48 / +0.36 | both halves | 9e-05 | ⚠ **readthrough risk**: GAPLINC lies 6.3 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[CDKN1B]] | +0.51 | +0.37 / +0.49 | both halves | 7e-05 |  |
| [[JADE2]] | +0.51 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[CHMP1B]] | +0.50 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[MKLN1-AS]] | +0.50 | +0.38 / +0.39 | both halves | 7e-05 |  |
| [[SOCS6]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[HIVEP2]] | +0.50 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[BCL6]] | +0.49 | +0.47 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 479 |
| [[NBR1]] | +0.49 | +0.36 / +0.46 | both halves | 9e-05 |  |
| [[CXCL3]] | +0.49 | +0.33 / +0.35 | both halves | 1e-04 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2A]] | -0.49 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[PPM1F]] | -0.46 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[DGKZ]] | -0.45 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[AP1M1]] | -0.43 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[EPN2]] | -0.43 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[SLC23A2]] | -0.43 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[ATG16L2]] | -0.42 | -0.26 / -0.36 | both halves | 4e-04 |  |
| [[CHAF1B]] | -0.42 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[KATNBL1]] | -0.42 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[DHDDS]] | -0.42 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[STAC]] | -0.42 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[SCAI]] | -0.42 | -0.37 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BATF]] | B | BATF activity lowers TGIF1's level | lines that do not express BATF (33) vs lines expressing it (17) | 1.30× higher at baseline in the lines without BATF | 0.012 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[SOD2]] | C | SOD2 activity lowers TGIF1's level | lines that do not express SOD2 (3) vs lines expressing it (47) | 2.57× higher at baseline in the lines without SOD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC9A3, SMOX, NDRG1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.434). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (31.9, 7.0); signed map (39.9, 2.8). **Vector** length 109, 28.2% of its response variance represented; |z| ≥ 3 in 1,224 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.4 | +14.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.6 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | +0.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.3 | +5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | -1.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +2.5 |
|  | [[Penfluridol (drug)]] 5 µM |  | +2.3 | +1.7 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -29.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -8.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -27.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.8 | -5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -5.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -6.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.4 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | TGFB induced factor homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.31 — chr18:3,411,608-3,459,978 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HPE4, TGIF |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Hallmark sets | TGF_BETA_SIGNALING, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 5 pathways, smallest: Downregulation of SMAD2/3:SMAD4 transcriptional activity; SMAD2/SMAD3:SMAD4 heterotrimer regulates transcription; Transcriptional activity of SMAD2/SMAD3:SMAD4 heterotrimer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15583](https://www.uniprot.org/uniprotkb/Q15583) (Homeobox protein TGIF1):

> Binds to a retinoid X receptor (RXR) responsive element from the cellular retinol-binding protein II promoter (CRBPII-RXRE). Inhibits the 9-cis-retinoic acid-dependent RXR alpha transcription activation of the retinoic acid responsive element. Active transcriptional corepressor of SMAD2. Links the nodal signaling pathway to the bifurcation of the forebrain and the establishment of ventral midline structures. May participate in the transmission of nuclear signals during development and in the …

**Summary**, from NCBI Gene [7050](https://www.ncbi.nlm.nih.gov/gene/7050):

> The protein encoded by this gene is a member of the three-amino acid loop extension (TALE) superclass of atypical homeodomains. TALE homeobox proteins are highly conserved transcription regulators. This particular homeodomain binds to a previously characterized retinoid X receptor responsive element from the cellular retinol-binding protein II promoter. In addition to its role in inhibiting 9-cis-retinoic acid-dependent RXR alpha transcription activation of the retinoic acid responsive element, …

**Accessions** — [HGNC:11776](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11776) · Entrez [7050](https://www.ncbi.nlm.nih.gov/gene/7050) · UniProt [Q15583](https://www.uniprot.org/uniprotkb/Q15583) · Ensembl [ENSG00000177426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177426)

## Data

Gene col 10821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10821); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10821]; `tensor/DDL_lfc|DDL_z.npy` [10821]; `embed/gene_vectors.npy` [10821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10821 or target_col == 10821). Every well: [[TGIF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/TGIF1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
